-- ============================================================
-- Supabase Database Migration
-- Run this in your Supabase project's SQL Editor
-- ============================================================

-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- ============================================================
-- PROFILES (extends auth.users)
-- ============================================================
create table if not exists public.profiles (
  id          uuid references auth.users on delete cascade primary key,
  email       text unique not null,
  nickname    text,
  created_at  timestamptz default now()
);

-- Auto-create profile on user signup
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, email, nickname)
  values (
    new.id,
    new.email,
    coalesce(new.raw_user_meta_data->>'nickname', split_part(new.email, '@', 1))
  );
  return new;
end;
$$ language plpgsql security definer;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

-- ============================================================
-- API KEYS (encrypted storage)
-- ============================================================
create table if not exists public.api_keys (
  id              uuid primary key default gen_random_uuid(),
  user_id         uuid references public.profiles(id) on delete cascade not null,
  provider        text check (provider in ('openai', 'anthropic')) not null,
  base_url        text default 'https://api.openai.com/v1',
  encrypted_key   text not null,
  iv              text not null,
  is_active       boolean default true,
  created_at      timestamptz default now()
);

create index if not exists api_keys_user_id_idx on public.api_keys(user_id);

-- ============================================================
-- TEXTBOOKS
-- ============================================================
create table if not exists public.textbooks (
  id            uuid primary key default gen_random_uuid(),
  user_id       uuid references public.profiles(id) on delete cascade not null,
  filename      text not null,
  storage_path  text not null,
  file_size     bigint,
  created_at    timestamptz default now()
);

create index if not exists textbooks_user_id_idx on public.textbooks(user_id);

-- ============================================================
-- CONVERSATIONS
-- ============================================================
create table if not exists public.conversations (
  id                    uuid primary key default gen_random_uuid(),
  user_id               uuid references public.profiles(id) on delete cascade not null,
  title                 text default '新对话',
  current_textbook_id   uuid references public.textbooks(id) on delete set null,
  created_at            timestamptz default now(),
  updated_at            timestamptz default now()
);

create index if not exists conversations_user_id_idx on public.conversations(user_id);

-- ============================================================
-- MESSAGES
-- ============================================================
create table if not exists public.messages (
  id              uuid primary key default gen_random_uuid(),
  conversation_id uuid references public.conversations(id) on delete cascade not null,
  role            text check (role in ('user', 'assistant', 'system')) not null,
  character       text check (character in ('mu', 'sang', null)),
  content         text not null,
  created_at      timestamptz default now()
);

create index if not exists messages_conversation_id_idx on public.messages(conversation_id);

-- ============================================================
-- CHARACTER STATES (global, cross-conversation)
-- ============================================================
create table if not exists public.character_states (
  id            uuid primary key default gen_random_uuid(),
  user_id       uuid references public.profiles(id) on delete cascade not null,
  character_id  text not null, -- 'mu' | 'sang' | etc.
  affection     integer default 50 check (affection between 0 and 100),
  strictness    integer default 50 check (strictness between 0 and 100),
  mood          jsonb default '{}',
  log           jsonb default '[]',
  updated_at    timestamptz default now(),
  unique(user_id, character_id)
);

create index if not exists character_states_user_id_idx on public.character_states(user_id);

-- Function to append to character log
create or replace function public.character_append_log(
  p_user_id       uuid,
  p_character_id  text,
  p_entry        text,
  p_timestamp    timestamptz
)
returns void as $$
begin
  update public.character_states
  set
    log = jsonb_insert(
      coalesce(log, '[]'::jsonb),
      to_jsonb(jsonb_array_length(coalesce(log, '[]'::jsonb))),
      jsonb_build_object('text', p_entry, 'date', p_timestamp)
    ),
    updated_at = p_timestamp
  where user_id = p_user_id and character_id = p_character_id;
end;
$$ language plpgsql;

-- ============================================================
-- DIARIES
-- ============================================================
create table if not exists public.diaries (
  id          uuid primary key default gen_random_uuid(),
  user_id     uuid references public.profiles(id) on delete cascade not null,
  date        date not null,
  content     text not null,
  created_at  timestamptz default now()
);

create index if not exists diaries_user_id_idx on public.diaries(user_id);
create index if not exists diaries_date_idx on public.diaries(date);

-- ============================================================
-- PROGRESS
-- ============================================================
create table if not exists public.progress (
  id              uuid primary key default gen_random_uuid(),
  user_id         uuid references public.profiles(id) on delete cascade not null,
  textbook_id     uuid references public.textbooks(id) on delete set null,
  conversation_id uuid references public.conversations(id) on delete set null,
  chapter         text,
  notes           text,
  mastery         text check (mastery in ('new', 'learning', 'mastered')) default 'new',
  created_at      timestamptz default now()
);

create index if not exists progress_user_id_idx on public.progress(user_id);

-- ============================================================
-- Row Level Security (RLS) — Essential for production
-- ============================================================

alter table public.profiles     enable row level security;
alter table public.api_keys     enable row level security;
alter table public.textbooks    enable row level security;
alter table public.conversations enable row level security;
alter table public.messages     enable row level security;
alter table public.character_states enable row level security;
alter table public.diaries      enable row level security;
alter table public.progress     enable row level security;

-- Profiles: users can only see/edit their own row
create policy "Users can view own profile"  on public.profiles for select using (auth.uid() = id);
create policy "Users can update own profile" on public.profiles for update using (auth.uid() = id);

-- API keys: users can only see/edit their own keys
create policy "Users can view own api_keys"   on public.api_keys for select using (auth.uid() = user_id);
create policy "Users can insert own api_keys" on public.api_keys for insert with check (auth.uid() = user_id);
create policy "Users can update own api_keys" on public.api_keys for update using (auth.uid() = user_id);

-- Textbooks
create policy "Users can view own textbooks"   on public.textbooks for select using (auth.uid() = user_id);
create policy "Users can insert own textbooks"  on public.textbooks for insert with check (auth.uid() = user_id);
create policy "Users can delete own textbooks"  on public.textbooks for delete using (auth.uid() = user_id);

-- Conversations
create policy "Users can view own conversations"   on public.conversations for select using (auth.uid() = user_id);
create policy "Users can insert own conversations" on public.conversations for insert with check (auth.uid() = user_id);
create policy "Users can update own conversations" on public.conversations for update using (auth.uid() = user_id);
create policy "Users can delete own conversations" on public.conversations for delete using (auth.uid() = user_id);

-- Messages
create policy "Users can view own messages"   on public.messages for select using (
  exists (select 1 from public.conversations where id = conversation_id and user_id = auth.uid())
);
create policy "Users can insert own messages" on public.messages for insert with check (
  exists (select 1 from public.conversations where id = conversation_id and user_id = auth.uid())
);

-- Character states
create policy "Users can view own character states"   on public.character_states for select using (auth.uid() = user_id);
create policy "Users can update own character states" on public.character_states for update using (auth.uid() = user_id);
create policy "Users can insert own character states" on public.character_states for insert with check (auth.uid() = user_id);

-- Diaries
create policy "Users can view own diaries" on public.diaries for select using (auth.uid() = user_id);
create policy "Users can insert own diaries" on public.diaries for insert with check (auth.uid() = user_id);

-- Progress
create policy "Users can view own progress"   on public.progress for select using (auth.uid() = user_id);
create policy "Users can insert own progress" on public.progress for insert with check (auth.uid() = user_id);
create policy "Users can update own progress" on public.progress for update using (auth.uid() = user_id);

-- ============================================================
-- Storage Bucket for Textbooks
-- Run this in Supabase Dashboard > Storage > New bucket
-- Or via SQL:
-- ============================================================
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('textbooks', 'textbooks', false, 10485760, array['text/markdown', 'text/plain'])
on conflict (id) do nothing;

create policy "Users can upload own textbooks" on storage.objects
  for insert with check (bucket_id = 'textbooks' and auth.uid()::text = (storage.foldername(name))[1]);

create policy "Users can view own textbooks" on storage.objects
  for select using (bucket_id = 'textbooks' and auth.uid()::text = (storage.foldername(name))[1]);

create policy "Users can delete own textbooks" on storage.objects
  for delete using (bucket_id = 'textbooks' and auth.uid()::text = (storage.foldername(name))[1]);

-- ============================================================
-- Done!
-- ============================================================
