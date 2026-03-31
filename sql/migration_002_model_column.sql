-- Migration: add model column and relax provider constraint
-- Run in Supabase SQL Editor

-- 1. Add model column to api_keys (nullable)
alter table public.api_keys
  add column if not exists model text;

-- 2. Drop the old provider check constraint (only allowed openai/anthropic)
--    and replace with a looser one that allows any string
alter table public.api_keys
  drop constraint if exists api_keys_provider_check;

-- (No new constraint needed — any provider string is now valid)

-- Done!
