# FederatedLearning

Yang Liu 
Yan Kang 
Han Yu

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/68cccd03769b70f4b0bb5db795c8d435f70d87e0afe0b221278b77a71a09ddf8.jpg)


SYNTHESIS LECTURES ON ARTIFICIALINTELLIGENCE AND MACHINE LEARNING

# Federated Learning

# Synthesis Lectures on ArtificialIntelligence and MachineLearning

Editors

Ronald J. Brachman, Jacobs Technion-Cornell Institute at Cornell Tech

Francesca Rossi, IBM Research AI

Peter Stone, University of Texas at Austin

Federated Learning

Qiang Yang, Yang Liu, Yong Cheng, Yan Kang, Tianjian Chen, and Han Yu2019

An Introduction to the Planning Domain Definition Language

Patrik Haslum, Nir Lipovetzky, Daniele Magazzeni, and Christian Muise2019

Reasoning with Probabilistic and Deterministic Graphical Models: Exact Algorithms,Second Edition

Rina Dechter

2019

Learning and Decision-Making from Rank Data

Lirong Xia

2019

Lifelong Machine Learning, Second Edition

Zhiyuan Chen and Bing Liu

2018

Adversarial Machine Learning

Yevgeniy Vorobeychik and Murat Kantarcioglu

2018

Strategic Voting

Reshef Meir

2018



Predicting Human Decision-Making: From Prediction to ActionAriel Rosenfeld and Sarit Kraus2018





Game Theory for Data Science: Eliciting Truthful InformationBoi Faltings and Goran Radanovic2017





Multi-Objective Decision MakingDiederik M. Roijers and Shimon Whiteson2017





Lifelong Machine LearningZhiyuan Chen and Bing Liu2016





Statistical Relational Artificial Intelligence: Logic, Probability, and ComputationLuc De Raedt, Kristian Kersting, Sriraam Natarajan, and David Poole2016





Representing and Reasoning with Qualitative Preferences: Tools and ApplicationsGanesh Ram Santhanam, Samik Basu, and Vasant Honavar2016





Metric LearningAurélien Bellet, Amaury Habrard, and Marc Sebban2015





Graph-Based Semi-Supervised LearningAmarnag Subramanya and Partha Pratim Talukdar2014





Robot Learning from Human TeachersSonia Chernova and Andrea L. Thomaz2014





General Game PlayingMichael Genesereth and Michael Thielscher2014





Judgment Aggregation: A PrimerDavide Grossi and Gabriella Pigozzi2014





An Introduction to Constraint-Based Temporal ReasoningRoman Barták, Robert A. Morris, and K. Brent Venable2014





Reasoning with Probabilistic and Deterministic Graphical Models: Exact AlgorithmsRina Dechter2013





Introduction to Intelligent Systems in Traffic and TransportationAna L.C. Bazzan and Franziska Klügl2013





A Concise Introduction to Models and Methods for Automated PlanningHector Geffner and Blai Bonet2013





Essential Principles for Autonomous RoboticsHenry Hexmoor2013





Case-Based Reasoning: A Concise IntroductionBeatriz López2013





Answer Set Solving in PracticeMartin Gebser, Roland Kaminski, Benjamin Kaufmann, and Torsten Schaub2012





Planning with Markov Decision Processes: An AI PerspectiveMausam and Andrey Kolobov2012





Active LearningBurr Settles2012





Computational Aspects of Cooperative Game TheoryGeorgios Chalkiadakis, Edith Elkind, and Michael Wooldridge2011





Representations and Techniques for 3D Object Recognition and Scene InterpretationDerek Hoiem and Silvio Savarese2011





A Short Introduction to Preferences: Between Artificial Intelligence and Social ChoiceFrancesca Rossi, Kristen Brent Venable, and Toby Walsh2011





Human ComputationEdith Law and Luis von Ahn2011



Trading Agents

Michael P. Wellman

2011

Visual Object Recognition

Kristen Grauman and Bastian Leibe

2011

Learning with Support Vector Machines

Colin Campbell and Yiming Ying

Algorithms for Reinforcement Learning

Csaba Szepesvári

Data Integration: The Relational Logic Approach

Michael Genesereth

Markov Logic: An Interface Layer for Artificial Intelligence

Pedro Domingos and Daniel Lowd

2009

Introduction to Semi-Supervised Learning

Xiaojin Zhu and Andrew B. Goldberg

Action Programming Languages

Michael Thielscher

Representation Discovery using Harmonic Analysis

Sridhar Mahadevan

Essentials of Game Theory: A Concise Multidisciplinary Introduction

Kevin Leyton-Brown and Yoav Shoham

2008

A Concise Introduction to Multiagent Systems and Distributed Artificial Intelligence

Nikos Vlassis

2007

Intelligent Autonomous Robotics: A Robot Soccer Case Study

Peter Stone

2007

Copyright $^ { © }$ 2020 by Morgan & Claypool

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted inany form or by any means—electronic, mechanical, photocopy, recording, or any other except for brief quotationsin printed reviews, without the prior permission of the publisher.

Federated Learning

Qiang Yang, Yang Liu, Yong Cheng, Yan Kang, Tianjian Chen, and Han Yu

www.morganclaypool.com

ISBN: 9781687336976 paperback

ISBN: 9781687336983 ebook

ISBN: 9781687336990 hardcover

DOI 10.2200/S00960ED2V01Y201910AIM043

A Publication in the Morgan & Claypool Publishers series

SYNTHESIS LECTURES ON ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING

Lecture #43

Series Editors: Ronald J. Brachman, Jacobs Technion-Cornell Institute at Cornell Tech

Francesca Rossi, IBM Research AI

Peter Stone, University of Texas at Austin

Series ISSN

Synthesis Lectures on Artificial Intelligence and Machine Learning

Print 1939-4608 Electronic 1939-4616

# Federated Learning

Qiang Yang

WeBank and Hong Kong University of Science and Technology, China

Yang Liu

WeBank, China

Yong Cheng

WeBank, China

Yan Kang

WeBank, China

Tianjian Chen

WeBank, China

Han Yu

Nanyang Technological University, Singapore

SYNTHESIS LECTURES ON ARTIFICIAL INTELLIGENCE ANDMACHINE LEARNING #43

# ABSTRACT

How is it possible to allow multiple data owners to collaboratively train and use a shared pre-diction model while keeping all the local training data private? Traditional machine learningapproaches need to combine all data at one location, typically a data center, which may verywell violate the laws on user privacy and data confidentiality. Today, many parts of the worlddemand that technology companies treat user data carefully according to user-privacy laws. TheEuropean Union’s General Data Protection Regulation (GDPR) is a prime example. In thisbook, we describe how federated machine learning addresses this problem with novel solutionscombining distributed machine learning, cryptography and security, and incentive mechanismdesign based on economic principles and game theory. We explain different types of privacy-preserving machine learning solutions and their technological backgrounds, and highlight somerepresentative practical use cases. We show how federated learning can become the foundation ofnext-generation machine learning that caters to technological and societal needs for responsibleAI development and application.

# KEYWORDS

federated learning, secure multi-party computation, privacy preserving machinelearning, machine learning algorithms, transfer learning, artificial intelligence, dataconfidentiality, GDPR, privacy regulations

# Contents

# Preface . xiii

# Acknowledgments xvii

# 1 Introduction

1.1 Motivation

1.2 Federated Learning as a Solution 3

1.2.1 The Definition of Federated Learning 4

1.2.2 Categories of Federated Learning

1.3 Current Development in Federated Learning . 10

1.3.1 Research Issues in Federated Learning 10

1.3.2 Open-Source Projects . 11

1.3.3 Standardization Efforts . . 13

1.3.4 The Federated AI Ecosystem 14

1.4 Organization of this Book 15

# 2 Background 17

2.1 Privacy-Preserving Machine Learning 17

2.2 PPML and Secure ML 17

2.3 Threat and Security Models 18

2.3.1 Privacy Threat Models 18

2.3.2 Adversary and Security Models 21

2.4 Privacy Preservation Techniques 21

2.4.1 Secure Multi-Party Computation . 21

2.4.2 Homomorphic Encryption . 26

2.4.3 Differential Privacy 29

# 3 Distributed Machine Learning 33

3.1 Introduction to DML 33

3.1.1 The Definition of DML 33

3.1.2 DML Platforms 35

3.2 Scalability-Motivated DML 36

3.2.1 Large-Scale Machine Learning 36

3.2.2 Scalability-Oriented DML Schemes . 37

# 3.3 Privacy-Motivated DML 40

3.3.1 Privacy-Preserving Decision Trees . . 40

3.3.2 Privacy-Preserving Techniques . 42

3.3.3 Privacy-Preserving DML Schemes 42

# 3.4 Privacy-Preserving Gradient Descent 45

3.4.1 Vanilla Federated Learning . 45

3.4.2 Privacy-Preserving Methods . 46

# 3.5 Summary 48

# 4 Horizontal Federated Learning 49

4.1 The Definition of HFL 49

4.2 Architecture of HFL 50

4.2.1 The Client-Server Architecture . 51

4.2.2 The Peer-to-Peer Architecture 53

4.2.3 Global Model Evaluation . . 54

4.3 The Federated Averaging Algorithm 55

4.3.1 Federated Optimization 55

4.3.2 The FedAvg Algorithm . 58

4.3.3 The Secured FedAvg Algorithm 60

4.4 Improvement of the FedAvg Algorithm 62

4.4.1 Communication Efficiency 62

4.4.2 Client Selection . 64

4.5 Related Works 64

4.6 Challenges and Outlook 66

# 5 Vertical Federated Learning 69

5.1 The Definition of VFL . 69

5.2 Architecture of VFL . 71

5.3 Algorithms of VFL 73

5.3.1 Secure Federated Linear Regression . . 73

5.3.2 Secure Federated Tree-Boosting . 76

5.4 Challenges and Outlook 81

# 6 Federated Transfer Learning 83

6.1 Heterogeneous Federated Learning . 83

6.2 Federated Transfer Learning 84

6.3 The FTL Framework 86

6.3.1 Additively Homomorphic Encryption . 88

6.3.2 The FTL Training Process 89

6.3.3 The FTL Prediction Process . . 90

6.3.4 Security Analysis . 90

6.3.5 Secret Sharing-Based FTL 91

6.4 Challenges and Outlook 92

# 7 Incentive Mechanism Design for Federated Learning 95

7.1 Paying for Contributions 95

7.1.1 Profit-Sharing Games . 95

7.1.2 Reverse Auctions . . 97

7.2 A Fairness-Aware Profit Sharing Framework . 98

7.2.1 Modeling Contribution 98

7.2.2 Modeling Cost 99

7.2.3 Modeling Regret . 100

7.2.4 Modeling Temporal Regret 100

7.2.5 The Policy Orchestrator 100

7.2.6 Computing Payoff Weightage 103

7.3 Discussions 103

# 8 Federated Learning for Vision, Language, and Recommendation 107

8.1 Federated Learning for Computer Vision . 107

8.1.1 Federated CV 107

8.1.2 Related Works . 109

8.1.3 Challenges and Outlook . 111

8.2 Federated Learning for NLP 112

8.2.1 Federated NLP 112

8.2.2 Related Works . . 113

8.2.3 Challenges and Outlook . 114

8.3 Federated Learning for Recommendation Systems 115

8.3.1 Recommendation Model 116

8.3.2 Federated Recommendation System 117

8.3.3 Related Works . 118

8.3.4 Challenges and Outlook . 119

# 9 Federated Reinforcement Learning 121

9.1 Introduction to Reinforcement Learning 121

9.1.1 Policy . 122

9.1.2 Reward 122

9.1.3 Value Function 122

9.1.4 Model of the Environment . 123

9.1.5 RL Background Example 123

9.2 Reinforcement Learning Algorithms 124

9.3 Distributed Reinforcement Learning 124

9.3.1 Asynchronous Distributed Reinforcement Learning . 125

9.3.2 Synchronous Distributed Reinforcement Learning . 126

9.4 Federated Reinforcement Learning 126

9.4.1 Background and Categorization . 126

9.5 Challenges and Outlook 131

# 10 Selected Applications 133

10.1 Finance 133

10.2 Healthcare 134

10.3 Education 136

10.4 Urban Computing and Smart City 136

10.5 Edge Computing and Internet of Things 139

10.6 Blockchain 140

10.7 5G Mobile Networks 141

# 11 Summary and Outlook . 143

# A Legal Development on Data Protection . 145

A.1 Data Protection in the European Union 145

A.1.1 The Terminology of GDPR 146

A.1.2 Highlights of GDPR 147

A.1.3 Impact of GDPR 150

A.2 Data Protection in the USA 151

A.3 Data Protection in China . 152

# Bibliography 155

# Authors’ Biographies 187

# Preface

This book is about how to build and use machine learning (ML) models in artificial intelligence(AI) applications when the data are scattered across different sites, owned by different individ-uals or organizations, and there is no easy solution to bring the data together. Nowadays, weoften hear that we are in the era of big data, and big data is an important ingredient that fuelsAI advances in today’s society. However, the truth is that we are in an era of small, isolated, andfragmented data silos. Data are collected and located at edge devices such as mobile phones.Organizations such as hospitals often have limited views on users’ data due to their specialties.However, privacy and security requirements make it increasingly infeasible to merge the data atdifferent organizations in a simple way. In such a context, federated machine learning (or fed-erated learning, in short) emerges as a functional solution that can help build high-performancemodels shared among multiple parties while still complying with requirements for user privacyand data confidentiality.

Besides privacy and security concerns, another strong motivation for federated learning isto maximally use the computing power at the edge devices of a cloud system, where the commu-nication is most efficient when only the computed results, rather than raw data, are transmittedbetween devices and servers. For example, autonomous cars can handle most computation lo-cally and exchange the required results with the cloud at intervals. Satellites can finish most ofthe computation for information that they are to gather and communicate with the earth-basedcomputers using minimal communication channels. Federated learning allows synchronizationof computation between multiple devices and computing servers by exchanging only computedresults.

We can explain federated learning with an analogy. That is, an ML model is like a sheepand the data is the grass. A traditional way to rear sheep is by buying the grass and transferringit to where the sheep is located, much like when we buy the datasets and move them to a centralserver. However, privacy concerns and regulations prevent us from physically moving the data.In our analogy, the grass can no longer travel outside its local area. Instead, federated learningemploys a dual methodology. We can let the sheep graze multiple grasslands, much like our MLmodel that is built in a distributed manner without the data traveling outside its local area. Inthe end, the ML model grows from everyone’s data, just like the sheep feed on everyone’s grass.

Today, our modern society demands more responsible use of AI, and user privacy anddata confidentiality are important properties of AI systems. In this direction, federated learn-ing is already making significant positive impact, ranging from securely updating user modelson mobile phones to improving medical imaging performance with multiple hospitals. Manyexisting works in different computer science areas have laid the foundation for the technology,

such as distributed optimization and learning, homomorphic encryption, differential privacy,and secure multi-party computation.

There are two types of federated learning, horizontal and vertical. The Google GBoard sys-tem adopts horizontal federated learning and shows an example of B2C (business-to-consumer)applications. It can also be used to support edge computing, where the devices at the edge of acloud system can handle many of the computing tasks and thus reduce the need to communi-cate via raw data with the central servers. Vertical federated learning, proposed and advanced byWeBank, represents the B2B (business-to-business) model, where multiple organizations joinan alliance in building and using a shared ML model. The model is built while ensuring thatno local data leaves any sites and maintaining the model performance according to businessrequirements. In this book, we cover both the B2C and B2B models.

To develop a federated learning system, multiple disciplines are needed, including ML al-gorithms, distributed machine learning (DML), cryptography and security, privacy-preservingdata mining, game theory and economic principles, incentive mechanism design, laws and reg-ulatory requirements, etc. It is a daunting task for someone to be well-versed in so many diversedisciplines, and the only sources for studying this field are currently scattered across many re-search papers and blogs. Therefore, there is a strong need for a comprehensive introduction tothis subject in a single text, which this book offers.

This book is an introduction to federated learning and can serve as one’s first entranceinto this subject area. It is written for students in computer science, AI, and ML, as well asfor big data and AI application developers. Students at senior undergraduate or graduate lev-els, faculty members, and researchers at universities and research institutions can find the bookuseful. Lawmakers, policy regulators, and government service departments can also consider itas a reference book on legal matters involving big data and AI. In classrooms, it can serve as atextbook for a graduate seminar course or as a reference book on federated learning literature.

The idea of this book came about in our development of a federated learning platform atWeBank known as Federated AI Technology Enabler (FATE), which became the world’s firstopen-source federated learning platform and is now part of the Linux Foundation. WeBankis a digital bank that serves hundreds of millions of people in China. This digital bank has abusiness alliance across diverse backgrounds, including banking, insurance, Internet, and retailand supply-chain companies, just to name a few. We observe firsthand that data cannot be easilyshared, but the need to collaborate to build new businesses supported by ML is very strong.

Federated learning was practiced by Google at large-scale in its mobile services for con-sumers as an example of B2C applications. We took one step further in expanding it to enablepartnerships between multiple businesses in a partnership for B2B applications. The horizon-tal, vertical, and transfer learning-based federated learning categorization was first summarizedin our survey paper published in ACM Transactions on Intelligent Systems and Technology (ACMTIST) [Yang et al., 2019] and was also presented at the 2019 AAAI Conference on Artifi-cial Intelligence (organized by the Association for the Advancement of Artificial Intelligence)

in Hawaii. Subsequently, various tutorials were given at conferences such as the 14th ChineseComputer Federation Technology Frontier in 2019. In the process of developing this book, ouropen-source federated learning system, FATE, was born and publicized [WeBank FATE, 2019](see https://www.fedai.org), and the first international standard on federated learning viaIEEE is being developed [IEEE P3652.1, 2019]. The tutorial notes and related research papersserved as the basis for this book.

Qiang Yang, Yang Liu, Yong Cheng, Yan Kang, Tianjian Chen, and Han YuNovember 2019, Shenzhen, China

# Acknowledgments

The writing of this book involved huge efforts from a group of very dedicated contributors.Besides the authors, different chapters were contributed by Ph.D. students, researchers, andresearch partners at various stages. We express our heartfelt gratitude to the following peoplewho have made contributions toward the writing and editing of this book.

• Dashan Gao helped with writing Chapters 2 and 3.

• Xueyang Wu helped with writing Chapters 3 and 5.

• Xinle Liang helped with writing Chapters 3 and 9.

• Yunfeng Huang helped with writing Chapters 5 and 8.

• Sheng Wan helped with writing Chapters 6 and 8.

• Xiguang Wei helped with writing Chapter 9.

• Pengwei Xing helped with writing Chapters 8 and 10.

Finally, we thank our family for their understanding and continued support. Withoutthem, the book would not have been possible.

Qiang Yang, Yang Liu, Yong Cheng, Yan Kang, Tianjian Chen, and Han YuNovember 2019, Shenzhen, China

# 1.1 MOTIVATION

We have witnessed the rapid growth of machine learning (ML) technologies in empoweringdiverse artificial intelligence (AI) applications, such as computer vision, automatic speech recog-nition, natural language processing, and recommender systems [Pouyanfar et al., 2019, Hatcherand Yu, 2018, Goodfellow et al., 2016]. The success of these ML technologies, in particulardeep learning (DL), has been fueled by the availability of vast amounts of data (a.k.a. the bigdata) [Trask, 2019, Pouyanfar et al., 2019, Hatcher and Yu, 2018]. Using these data, DL systemscan perform a variety of tasks that can sometimes exceed human performance; for example, DLempowered face-recognition systems can achieve commercially acceptable levels of performancegiven millions of training images. These systems typically require a huge amount of data to reacha satisfying level of performance. For example, the object detection system from Facebook hasbeen reported to be trained on 3.5 billion images from Instagram [Hartmann, 2019].

In general, the big data required to empower AI applications is often large in size. How-ever, in many application domains, people have found that big data are hard to come by. Whatwe have most of the time are “small data,” where either the data are of small sizes only, or theylack certain important information, such as missing values or missing labels. To provide suffi-cient labels for data often requires much effort from domain experts. For example, in medicalimage analysis, doctors are often employed to provide diagnosis based on scan images of patientorgans, which is tedious and time consuming. As a result, high-quality and large-volume train-ing data often cannot be obtained. Instead, we face silos of data that cannot be easily bridged.

The modern society is increasingly made aware of issues regarding the data ownership:who has the right to use the data for building AI technologies? In an AI-driven product rec-ommendation service, the service owner claims ownership over the data about the products andpurchase transactions, but the ownership over the data about user purchasing behaviors andpayment habits is unclear. Since data are generated and owned by different parties and organi-zations, a traditional and naive approach is to collect and transfer the data to one central locationwhere powerful computers can train and build ML models. Today, this methodology is no longervalid.

While AI is spreading into ever-widening application sectors, concerns regarding userprivacy and data confidentiality expand. Users are increasingly concerned that their private in-formation is being used (or even abused) by commercial and political purposes without theirpermission. Recently, several large Internet corporations have been fined heavily due to their

# 2 1. INTRODUCTION

leakage of users’ private data to commercial companies. Spammers and under-the-table dataexchanges are often punished in court cases.

In the legal front, law makers and regulatory bodies are coming up with new laws rulinghow data should be managed and used. One prominent example is the adoption of the GeneralData Protection Regulation (GDPR) by the European Union (EU) in 2018 [GDPR website,2018]. In the U.S., the California Consumer Privacy Act (CCPA) will be enacted in 2020 inthe state of California [DLA Piper, 2019]. China’s Cyber Security Law and the General Pro-visions of Civil Law, implemented in 2017, also imposed strict controls on data collection andtransactions. Appendix A provides more information about these new data protection laws andregulations.

Under this new legislative landscape, collecting and sharing data among different organi-zations is becoming increasingly difficult, if not outright impossible, as time goes by. In addition,the sensitive nature of certain data (e.g., financial transactions and medical records) prohibitsfree data circulation and forces the data to exist in isolated data silos maintained by the dataowners [Yang et al., 2019]. Due to industry competition, user privacy, data security, and com-plicated administrative procedures, even data integration between different departments of thesame company faces heavy resistance. The prohibitively high cost makes it almost impossible tointegrate data scattered in different institutions [WeBank AI, 2019]. Now that the old privacy-intrusive way of collecting and sharing data is outlawed, data consolidation involving differentdata owners is extremely challenging going forward.

How to solve the problem of data fragmentation and isolation while complying with thenew stricter privacy-protection laws is a major challenge for AI researchers and practitioners.Failure to adequately address this problem will likely lead to a new AI winter [Yang et al., 2019].

Another reason why the AI industry is facing a data plight is that the benefit of col-laborating over the sharing of the big data is not clear. Suppose that two organizations wishto collaborate on medical data in order to train a joint ML model. The traditional method oftransferring the data from one organization to another will often mean that the original dataowner will lose control over the data that they owned in the first place. The value of the datadecreases as soon as the data leaves the door. Furthermore, when the better model as a resultof integrating the data sources gained benefit, it is not clear how the benefit is fairly distributedamong the participants. This fear of losing control and lack of transparency in determining thedistribution of values is causing the so-called data fragmentation to intensify.

With edge computing over the Internet of Things, the big data is often not a single mono-lithic entity but rather distributed among many parties. For example, satellites taking images ofthe Earth cannot expect to transmit all data to data centers on the ground, as the amount oftransmission required will be too large. Likewise, with autonomous cars, each car must be ableto process much information locally with ML models while collaborate globally with other carsand computing centers. How to enable the updating and sharing of models among the multiplesites in a secure and yet efficient way is a new challenge to the current computing methodologies.

# 1.2 FEDERATED LEARNING AS A SOLUTION

As mentioned previously, multiple reasons make the problem of data silos become impedimentto the big data needed to train ML models. It is thus natural to seek solutions to build MLmodels that do not rely on collecting all data to a centralized storage where model training canhappen. An idea is to train a model at each location where a data source resides, and then letthe sites communicate their respective models in order to reach a consensus for a global model.In order to ensure user privacy and data confidentiality, the communication process is carefullyengineered so that no site can second-guess the private data of any other sites. At the sametime, the model is built as if the data sources were combined. This is the idea behind “federatedmachine learning” or “federated learning” for short.

Federated learning was first practiced in an edge-server architecture by McMahan etal. in the context of updating language models on mobile phones [McMahan et al., 2016a,b,Konecný et al., 2016a,b]. There are many mobile edge devices each holding private data. Toupdate the prediction models in the Gboard system, which is the Google’s keyboard systemfor auto-completion of words, researchers at Google developed a federated learning system toupdate a collective model periodically. Users of the Gboard system gets a suggested query andwhether the users clicked the suggested words. The word-prediction model in Gboard keepsimproving based on not just a single mobile phone’s accumulated data but all phones via a tech-nique known as federated averaging (FedAvg). Federated averaging does not require movingdata from any edge device to one central location. Instead, with federated learning, the modelon each mobile device, which can be a smartphones or a tablet, gets encrypted and shipped tothe cloud. All encrypted models are integrated into a global model under encryption, so thatthe server at the cloud does not know the data on each device [Yang et al., 2019, McMahan etal., 2016a,b, Konecný et al., 2016a,b, Hartmann, 2018, Liu et al., 2019]. The updated model,which is under encryption, is then downloaded to all individual devices on the edge of the cloudsystem [Konecný et al., 2016b, Hartmann, 2018, Yang et al., 2018, Hard et al., 2018]. In theprocess, users’ individual data on each device is not revealed to others, nor to the servers in thecloud.

Google’s federated learning system shows a good example of B2C (business-to-consumer), in designing a secure distributed learning environment for B2C applications. In theB2C setting, federated learning can ensure privacy protection as well as increased performancedue to a speedup in transmitting the information between the edge devices and the central server.

Besides the B2C model, federated learning can also support the B2B (business-to-business) model. In federated learning, a fundamental change in algorithmic design method-ology is, instead of transferring data from sites to sites, we transfer model parameters in a secureway, so that other parties cannot “second guess” the content of others’ data. Below, we give aformal categorization of the federated learning in terms of how the data is distributed amongthe different parties.

# 4 1. INTRODUCTION

# 1.2.1 THE DEFINITION OF FEDERATED LEARNING

Federated learning aims to build a joint ML model based on the data located at multiple sites.There are two processes in federated learning: model training and model inference. In the processof model training, information can be exchanged between parties but not the data. The exchangedoes not reveal any protected private portions of the data at each site. The trained model canreside at one party or shared among multiple parties.

At inference time, the model is applied to a new data instance. For example, in a B2Bsetting, a federated medical-imaging system may receive a new patient who’s diagnosis comefrom different hospitals. In this case, the parties collaborate in making a prediction. Finally,there should be a fair value-distribution mechanism to share the profit gained by the collaborativemodel. Mechanism design should done in such a way to make the federation sustainable.

In broad terms, federated learning is an algorithmic framework for building ML modelsthat can be characterized by the following features, where a model is a function mapping a datainstance at some party to an outcome.

• There are two or more parties interested in jointly building an ML model. Each partyholds some data that it wishes to contribute to training the model.

• In the model-training process, the data held by each party does not leave that party.

• The model can be transferred in part from one party to another under an encryptionscheme, such that other parties cannot re-engineer the data at any given party.

• The performance of the resulting model is a good approximation of ideal model built withall data transferred to a single party.

More formally, consider $N$ data owners $\{ \mathcal { F } _ { i } \} _ { i = 1 } ^ { N }$ who wish to train a ML model by usingtheir respective datasets $\{ \mathcal { D } _ { i } \} _ { i = 1 } ^ { N }$ 1 iD1. A conventional approach is to collect all data $\{ \mathcal { D } _ { i } \} _ { i = 1 } ^ { N }$ togetherat one data server and train a ML model $\mathcal { M } _ { S U M }$ on the server using the centralized dataset. Inthe conventional approach, any data owner $\{ \mathcal { F } _ { i }$ will expose its data $\{ \mathcal { D } _ { i }$ to the server and evenother data owners.

Federated learning is a ML process in which the data owners collaboratively train a model$\mathcal { M } _ { F E D }$ without collecting all data $\bar { \{ \mathcal { D } _ { i } \} } _ { i = 1 } ^ { N }$ . Denote $\gamma _ { S U M }$ and $\mathcal { V } _ { F E D }$ as the performance measure(e.g., accuracy, recall, and F1-score) of the centralized model $\mathcal { M } _ { S U M }$ and the federated model$\mathcal { M } _ { F E D }$ , respectively.

We can capture what we mean by performance guarantee more precisely. Let ı be a non-negative real number. We say that the federated learning model $\mathcal { M } _ { F E D }$ has $\delta$ -performance lossif

$$
\left| \mathcal {V} _ {S U M} - \mathcal {V} _ {F E D} \right| <   \delta . \tag {1.1}
$$

The previous equation expresses the following intuition: if we use secure federated learning tobuild a ML model on distributed data sources, this model’s performance on future data is ap-proximately the same as the model that is built on joining all data sources together.

We allow the federated learning system to perform a little less than a joint model becausein federated learning data owners do not expose their data to a central server or any other dataowners. This additional security and privacy guarantee can be worth a lot more than the loss inaccuracy, which is the ı value.

A federated learning system may or may not involve a central coordinating computerdepending on the application. An example involving a coordinator in a federated learning ar-chitecture is shown in Figure 1.1. In this setting, the coordinator is a central aggregation server(a.k.a. the parameter server), which sends an initial model to the local data owners A–C (a.k.a.clients or participants). The local data owners A–C each train a model using their respectivedataset, and send the model weight updates to the aggregation server. The aggregation severthen combines the model updates received from the data owners (e.g., using federated averag-ing [McMahan et al., 2016a]), and sends the combined model updates back to the local dataowners. This procedure is repeated until the model converges or until the maximum number ofiterations is reached. Under this architecture, the raw data of the local data owners never leavesthe local data owners. This approach not only ensures user privacy and data security, but alsosaves communication overhead needed to send raw data. The communication between the cen-tral aggregation server and the local data owners can be encrypted (e.g., using homomorphicencryption [Yang et al., 2019, Liu et al., 2019]) to guard against information leakage.

The federated learning architecture can also be designed in a peer to peer manner, whichdoes not require a coordinator. This ensures further security guarantee in which the parties com-municate directly without the help of a third party, as illustrated in Figure 1.2. The advantage ofthis architecture is increased security, but a drawback is potentially more computation to encryptand decrypt messages.

Federated learning brings several benefits. It preserves user privacy and data security bydesign since no data transfer is required. Federated learning also enables several parties to collab-oratively train a ML model so that each of the parties can enjoy a better model than what it canachieve alone. For example, federated learning can be used by private commercial banks to detectmulti-party borrowing, which has always been a headache in the banking industry, especially inthe Internet finance industry [WeBank AI, 2019]. With federated learning, there is no need toestablish a central database, and any financial institution participating in federated learning caninitiate new user queries to other agencies within the federation. Other agencies only need toanswer questions about local lending without knowing specific information of the user. This notonly protects user privacy and data integrity, but also achieves an important business objectiveof identifying multi-party lending.

While federated learning has great potential, it also faces several challenges. The com-munication link between the local data owner and the aggregation server may be slow and un-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/b9263e87badfea31fe3f088a948c24cad87006726b27df426e195bd9e1026f4e.jpg)



Figure 1.1: An example federated learning architecture: client-server model.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/048549e8fa832ad29a7c590a5871e60110688d173c77b49d9ddbbbcdc1385cb6.jpg)



Figure 1.2: An example federated learning architecture: peer-to-peer model.


stable [Hartmann, 2018]. There may be a very large number of local data owners (e.g., mobileusers). In theory, every mobile user can participate in federated learning, making the systemunstable and unpredictable. Data from different participants in federated learning may follownon-identical distributions [Zhao et al., 2018, Sattler et al., 2019, van Lier, 2018], and differentparticipants may have unbalanced numbers of data samples, which may result in a biased model

or even failure of training a model. As the participants are distributed and difficult to authen-ticate, federated learning model poisoning attacks [Bhagoji et al., 2019, Han, 2019], in whichone or more malicious participants send ruinous model updates to make the federated modeluseless, can take place and confound the whole operation.

# 1.2.2 CATEGORIES OF FEDERATED LEARNING

Let matrix $\mathcal { D } _ { i }$ denote the data held by the ith data owner. Suppose that each row of the matrix $\mathcal { D } _ { i }$represents a data sample, and each column represents a specific feature. At the same time, somedatasets may also contain label data. We denote the feature space as $\mathcal { X }$ , the label space as $\mathcal { V }$ , andwe use $\mathcal { T }$ to denote the sample ID space. For example, in the financial field, labels may be users’credit. In the marketing field labels may be the user’s purchasing desire. In the education field, $\mathcal { V }$may be the students’ scores. The feature $\mathcal { X }$ , label $\mathcal { V }$ , and sample IDs $\mathcal { T }$ constitute the completetraining dataset $( \boldsymbol { \mathcal { T } } , \boldsymbol { \mathcal { X } } , \boldsymbol { \mathcal { V } } )$ . The feature and sample spaces of the datasets of the participantsmay not be identical. We classify federated learning into horizontal federated learning (HFL),vertical federated learning (VFL), and federated transfer learning (FTL), according to how datais partitioned among various parties in the feature and sample spaces. Figures 1.3–1.5 show thethree federated learning categories for a two-party scenario [Yang et al., 2019].

HFL refers to the case where the participants in federated learning share overlapping datafeatures, i.e., the data features are aligned across the participants, but they differ in data samples.It resembles the situation that the data is horizontally partitioned inside a tabular view. Hence,we also call HFL as sample-partitioned federated learning, or example-partitioned federatedlearning [Kairouz et al., 2019]. Different from HFL, VFL applies to the scenario where the par-ticipants in federated learning share overlapping data samples, i.e., the data samples are alignedamongst the participants, but they differ in data features. It resembles the situation that data isvertically partitioned inside a tabular view. Thus, we also name VFL as feature-partitioned fed-erated learning. FTL is applicable for the case when there is neither overlapping in data samplesnor in features.

For example, when the two parties are two banks that serve two different regional mar-kets, they may share only a handful of users but their data may have very similar feature spacesdue to similar business models. That is, with limited overlap in users but large overlap in datafeatures, the two banks can collaborate in building ML models through horizontal federatedlearning [Yang et al., 2019, Liu et al., 2019].

When two parties providing different services but sharing a large amount of users (e.g.,a bank and an e-commerce company), they can collaborate on the different feature spaces thatthey own, leading to a better ML model for both. That is, with large overlap in users but littleoverlap in data features, the two companies can collaborate in building ML models throughvertical federated learning [Yang et al., 2019, Liu et al., 2019]. Split learning, recently proposedby Gupta and Raskar [2018] and Vepakomma et al. [2019, 2018], is regarded here as a specialcase of vertical federated learning, which enables vertically federated training of deep neural

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/82adde40778a35bb3fb2b0661649bd876b78f2d88cca70acf38409172114b5d8.jpg)



Figure 1.3: Illustration of HFL, a.k.a. sample-partitioned federated learning where the over-lapping features from data samples held by different participants are taken to jointly train amodel [Yang et al., 2019].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/f028f5996dd48189de2ec25d18d04190ddeaa30a05f5ec6d6e43aa2c55d419f9.jpg)



Figure 1.4: Illustration of VFL, a.k.a feature-partitioned federated learning where the overlap-ping data samples that have non-overlapping or partially overlapping features held by multipleparticipants are taken to jointly train a model [Yang et al., 2019].


networks (DNNs). That is, split learning facilitates training DNNs in federated learning settingsover vertically partitioned data [Vepakomma et al., 2019].

In scenarios where participating parties have highly heterogeneous data (e.g., distributionmismatch, domain shift, limited overlapping samples, and scarce labels), HFL and VFL maynot be able to build effective ML models. In those scenarios, we can leverage transfer learning

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/12797f24d58c5d4a201ef9fff7252724ce26061584782c66f1b1ba25d6252d75.jpg)



Figure 1.5: Federated transfer learning (FTL) [Yang et al., 2019]. A predictive model learnedfrom feature representations of aligned samples belonging to party A and party B is utilized topredict labels for unlabeled samples of party A.


techniques to bridge the gap between heterogeneous data owned by different parties. We referto federated learning leveraging transfer learning techniques as FTL.

Transfer learning aims to build effective ML models in a resource-scarce target domainby exploiting or transferring knowledge learned from a resource-rich source domain, which nat-urally fits the federated learning setting where parties are typically from different domains. Panand Yang [2010] divides transfer learning into mainly three categories: (i) instance-based trans-fer, (ii) feature-based transfer, and (iii) model-based transfer. Here, we provide brief descriptionson how these three categories of transfer learning techniques can be applied to federated settings.

• Instance-based FTL. Participating parties selectively pick or re-weight their training datasamples such that the distance among domain distributions can be minimized, therebyminimizing the objective loss function.

• Feature-based FTL. Participating parties collaboratively learn a common feature repre-sentation space, in which the distribution and semantic difference among feature repre-sentations transformed from raw data can be relieved and such that knowledge can betransferable across different domains to build more robust and accurate shared ML mod-els.

Figure 1.5 illustrates an FTL scenario where a predictive model learned from feature rep-resentations of aligned samples belonging to party A and party B is utilized to predictlabels for unlabeled samples of party A. We will elaborate on how this FTL is performedin Chapter 6.

• Model-based FTL. Participating parties collaboratively learn shared models that can ben-efit for transfer learning. Alternatively, participating parties can utilize pre-trained modelsas the whole or part of the initial models for a federated learning task.

We will further explain in detail the HFL and VFL in Chapter 4 and Chapter 5, respec-tively. In Chapter 6, we will elaborate on a feature-based FTL framework proposed by Liu etal. [2019].

# 1.3 CURRENT DEVELOPMENT IN FEDERATEDLEARNING

The idea of federated learning has appeared in different forms throughout the history ofcomputer science, such as privacy-preserving ML [Fang and Yang, 2008, Mohassel andZhang, 2017, Vaidya and Clifton, 2004, Xu et al., 2015], privacy-preserving DL [Liu et al.,2016, Phong, 2017, Phong et al., 2018], collaborative ML [Melis et al., 2018], collaborativeDL [Zhang et al., 2018, Hitaj et al., 2017], distributed ML [Li et al., 2014, Wang, 2016],distributed DL [Vepakomma et al., 2018, Dean et al., 2012, Ben-Nun and Hoefler, 2018],and federated optimization [Li et al., 2019, Xie et al., 2019], as well as privacy-preserving dataanalytics [Mangasarian et al., 2008, Mendes and Vilela, 2017, Wild and Mangasarian, 2007,Bogdanov et al., 2014]. Chapters 2 and 3 will present some examples.

# 1.3.1 RESEARCH ISSUES IN FEDERATED LEARNING

Federated learning was studied by Google in a research paper published in 2016 on arXiv.1 Sincethen, it has been an area of active research in the AI community as evidenced by the fast-growingvolume of preprints appearing on arXiv. Yang et al. [2019] provide a comprehensive survey ofrecent advances of federated learning.

Recent research work on federated learning are mainly focused on improving security andstatistical challenges [Yang et al., 2019, Mancuso et al., 2019]. Cheng et al. [2019] proposed Se-cureBoost in the setting of vertical federated learning, which is a novel lossless privacy-preservingtree-boosting system. SecureBoost provides the same level of accuracy as the non-privacy-preserving approach. It is theoretically proven that the SecureBoost framework is as accurate asother non-federated gradient tree-boosting algorithms that rely on centralized datasets [Chenget al., 2019].

Liu et al. [2019] presents a flexible federated transfer learning framework that can be effec-tively adapted to various secure multi-party ML tasks. In this framework, the federation allowsknowledge to be shared without compromising user privacy, and enables complimentary knowl-edge to be transferred in the network via transfer learning. As a result, a target-domain party canbuild more flexible and powerful models by leveraging rich labels from a source-domain party.

In a federated learning system, we can assume that participating parties are honest, semi-honest, or malicious. When a party is malicious, it is possible for a model to taint its data intraining. The possibility of model poisoning attacks on federated learning initiated by a singlenon-colluding malicious agent is discussed in Bhagoji et al. [2019]. A number of strategies tocarry out model poisoning attack were investigated. It was shown that even a highly constrainedadversary can carry out model poisoning attacks while simultaneously maintaining stealth. Thework of Bhagoji et al. [2019] reveals the vulnerability of the federated learning settings andadvocates the need to develop effective defense strategies.

Re-examining the existing ML models under the federated learning settings has become anew research direction. For example, combining federated learning with reinforcement learninghas been studied in Zhuo et al. [2019], where Gaussian differentials on the information sharedamong agents when updating their local models were applied to protect the privacy of data andmodels. It has been shown that the proposed federated reinforcement learning model performsclose to the baselines that directly take all joint information as input [Zhuo et al., 2019].

Another study in Smith et al. [2017] showed that multi-task learning is naturally suitedto handle the statistical challenges of federated learning, where separate but related models arelearned simultaneously at each node. The practical issues, such as communication cost, stragglers,and fault tolerance in distributed multi-task learning and federated learning, were considered. Anovel systems-aware optimization method was put forward, which achieves significant improvedefficiency compared to the alternatives.

Federated learning has also been applied in the fields of computer vision (CV ), e.g., med-ical image analysis [Sheller et al., 2018, Liu et al., 2018, Huang and Liu, 2019], natural lan-guage processing (NLP) (see, e.g., Chen et al. [2019]), and recommender systems (RS) (see,e.g., Ammad-ud-din et al. [2019]). This will be further reviewed in Chapter 8.

Regarding applications of federated learning, the researchers at Google have applied fed-erated learning in mobile keyboard prediction [Bonawitz and Eichner et al., 2019, Yang et al.,2018, Hard et al., 2018], which has achieved significant improvement in prediction accuracywithout exposing mobile user data. Researchers at Firefox have used federated learning for searchword prediction [Hartmann, 2018]. There is also new research effort to make federated learningmore personalizable [Smith et al., 2017, Chen et al., 2018].

# 1.3.2 OPEN-SOURCE PROJECTS

Interest in federated learning is not only limited to theoretical work. Research on the develop-ment and deployment of federated learning algorithms and systems is also flourishing. There areseveral fast-growing open-source projects of federated learning.

 Federated AI Technology Enabler (FATE) [WeBank FATE, 2019] is an open-sourceproject initiated by the AI department of WeBank2 to provide a secure computing framework tosupport the federated AI ecosystem [WeBank FedAI, 2019]. It implements secure computationprotocols based on homomorphic encryption (HE) and secure multi-party computation (MPC).It supports a range of federated learning architectures and secure computation algorithms, in-cluding logistic regression, tree-based algorithms, DL (artificial neural networks), and transferlearning. For more information on FATE, readers can refer to the GitHub FATE website [We-Bank FATE, 2019] and the FedAI website [WeBank FedAI, 2019].

 TensorFlow3 Federated project [Han, 2019, TFF, 2019, Ingerman and Ostrowski,2019, Tensorflow-federated, 2019] (TFF) is an open-source framework for experimenting withfederated ML and other computations on decentralized datasets. TFF enables developers tosimulate existing federated learning algorithms on their models and data, as well as to experi-ment with novel algorithms. The building blocks provided by TFF can also be used to implementnon-learning computations, such as aggregated analytics over decentralized data. The interfacesof TFF are organized in two layers: (1) the federated learning (FL) application programminginterface (API) and (2) federated Core (FC) API. TFF enables developers to declaratively ex-press federated computations, so that they can be deployed in diverse runtime environments.Included in TFF is a single-machine simulation run-time for experimentation.

 TensorFlow-Encrypted [TensorFlow-encrypted, 2019] is a Python library built on topof TensorFlow for researchers and practitioners to experiment with privacy-preserving ML. Itprovides an interface similar to that of TensorFlow, and aims to make the technology readilyavailable without requiring user to be experts in ML, cryptography, distributed systems, andhigh-performance computing.

 coMind [coMind.org, 2018, coMindOrg, 2019] is an open-source project for trainingprivacy-preserving federated DL models. The key component of coMind is the implementationof the federated averaging algorithm [McMahan et al., 2016a, Yu et al., 2018], which is trainingML models in a collaborative way while preserving user privacy and data security. coMind is builton top of TensorFlow and provides high-level APIs for implementing federated learning.

 Horovod [Sergeev and Balso, 2018, Horovod, 2019], developed by Uber, is an open-source distributed training framework for DL. It is based on the open message passing interface

(MPI) and works on top of popular DL frameworks, such as TensorFlow and PyTorch.4 Thegoal of Horovod is to make distributed DL fast and easy to use. Horovod supports federatedlearning via open MPI and currently, encryption is not yet supported.

 OpenMined/PySyft [Han, 2019, OpenMined, 2019, Ryffel et al., 2018, PySyft, 2019,Ryffel, 2019] provides two methods for privacy preservation: (1) federated learning and (2) dif-ferential privacy. OpenMined further supports two methods of secure computation throughmulti-party computation and homomorphic encryption. OpenMined has made available thePySyft library [PySyft, 2019], which is the first open-source federated learning framework forbuilding secure and scalable ML models [Ryffel, 2019]. PySyft is simply a hooked extension ofPyTorch. For users who are familiar with PyTorch, it is very easy to implement federated learn-ing systems with PySyft. Federated learning extension based on the TensorFlow framework iscurrently being developed within OpenMined.

LEAF Beanchmark [LEAF, 2019, Caldas et al., 2019], maintained by Carnegie MellonUniversity and Google AI, is a modular benchmarking framework for ML in federated settings,with applications in federated learning, multi-task learning, meta-learning, and on-device learn-ing. LEAF includes a suite of open-source federated datasets (e.g., FEMNIST, Sentiment140,and Shakespeare), a rigorous evaluation framework, and a set of reference implementations, aim-ing to capture the reality, obstacles, and intricacies of practical federated learning environments.LEAF enables researchers and practitioners in these domains to investigate new proposed so-lutions under more realistic assumptions and settings. LEAF will include additional tasks anddatasets in its future releases.

# 1.3.3 STANDARDIZATION EFFORTS

As more developments are made in the legal front on the secure and responsible use of users’ data,technical standard needs to be developed to ensure that organizations use the same language andfollow a standard guideline in developing future federated learning systems. Moreover, thereis increasing need for the technical community to communicate with the regulatory and legalcommunities over the use of the technology. As a result, it is important to develop internationalstandards that can be adopted by multiple disciplines.

For example, companies striving to satisfy the GDPR requirements need to know whattechnical developments are needed in order to satisfy the legal requirements. Standards canprovide a bridge between regulators and technical developers.

One of the early standards is initiated by the AI Department at WeBank with the Instituteof Electrical and Electronics Engineers (IEEE) P3652.1 Federated Machine Learning WorkingGroup (known as Federated Machine Learning (C/LT/FML)) was established in December

# 14 1. INTRODUCTION

2018 [IEEE P3652.1, 2019]. The objective of this working group is to provide guidelines forbuilding the architectural framework and applications of federated ML. The working group willdefine the architectural framework and application guidelines for federated ML, including:

1. The description and definition of federated learning;

2. The types of federated learning and the application scenarios to which each type applies;

3. Performance evaluation of federated learning; and

4. The associated regulatory requirements.

The purpose of this standard is to provide a feasible solution for the industrial applica-tion of AI without exchanging data directly. This standard is expected to promote and facilitatecollaborations in an environment where privacy and data protection issues have become increas-ingly important. It will promote and enable to the use of distributed data sources for the purposeof developing AI without violating regulations or ethical concerns.

# 1.3.4 THE FEDERATED AI ECOSYSTEM

The Federated AI (FedAI) ecosystem project was initiated by the AI Department of We-Bank [WeBank FedAI, 2019]. The primary goal of the project is to develop and promote ad-vanced AI technologies that preserve user privacy, data security, and data confidentiality. Thefederated AI ecosystem features four main themes.

• Open-source technologies: FedAI aims to accelerate open-source development of feder-ated ML and its applications. The FATE project [WeBank FATE, 2019] is a flagshipproject under FedAI.

• Standards and guidelines: FedAI, together with partners, are drawing up standardizationto formulate the architectural framework and application guidelines of federated learn-ing, and facilitate industry collaboration. One representative work is the IEEE P3652.1federated ML working group [IEEE P3652.1, 2019].

• Multi-party consensus mechanisms: FedAI is studying incentive and reward mechanismsto encourage more institutions to participate in federated learning research and develop-ment in a sustainable way. For example, FedAI is undertaking work to establish a multi-party consensus mechanism based on technologies like blockchain.

• Applications in various verticals: To open up the potential of federated learning, FedAIendeavors to showcase more vertical field applications and scenarios, and to build newbusiness models.

# 1.4 ORGANIZATION OF THIS BOOK

The organization of this book is as follows. Chapter 2 provides background information onprivacy-preserving ML, covering well-known techniques for data security. Chapter 3 describesdistributed ML, highlighting the difference between federated learning and distributed ML.Horizontal federated learning, vertical federated learning, and federated transfer learning areelaborated in detail in Chapter 4, Chapter 5, and Chapter 6, respectively. Incentive mecha-nism design for motivating the participation in federated learning is discussed in Chapter 7.Recent work on extending federated learning to the fields of computer vision, natural languageprocessing, and recommender systems are reviewed in Chapter 8. Chapter 9 presents federatedreinforcement learning. The prospect of applying federated learning into various industrial sec-tors is summarized in Chapter 10. Finally, we provide a summary of this book and looking aheadin Chapter 11. Appendix A provides an overview of recent data protection laws and regulationsin the European Union, the United States, and China.

# Background

In this chapter, we introduce the background knowledge related to federated learning, coveringprivacy-preserving machine learning techniques and data analytics.

# 2.1 PRIVACY-PRESERVING MACHINE LEARNING

Data leakage and privacy violation incidents have brought about heightened public awareness ofthe need for AI systems to be able to preserve user privacy and data confidentiality. Researchersare interested in developing techniques for privacy-preserving properties to be built inside ma-chine learning (ML) systems. The resulting systems are known as privacy-preserving machinelearning systems (PPML). In fact, 2018 was considered a breakout year for PPML [Mancuso etal., 2019]. PPML is a broad term that generally refers to ML equipped with defense measuresfor protecting user privacy and data security. The system security and cryptography communityhas also proposed various secure frameworks for ML.

In Westin [1968], Westin defined information privacy as follows: “the claim of individuals,groups, or institutions to determine for themselves when, how, and to what extent informationabout them is communicated to others.” This essentially defines the right to control the accessand handling of one’s information. The main idea of information privacy is to have control overthe collection and handling of one’s personal data [Mendes and Vilela, 2017].

In this chapter, we will introduce several popular approaches used in PPML includingsecure multi-party computation (MPC), homomorphic encryption (HE) for privacy-preservingmodel training and inference, as well as differential privacy (DP) for preventing unwanted datadisclosure. Privacy-preserving gradient descent methods will also be discussed.

# 2.2 PPML AND SECURE ML

Before going into the details of PPML, we first clarify the difference between PPML and secureML. PPML and secure ML differ mainly in the types of security violations that they are de-signed to deal with [Barreno et al., 2006]. In secure ML, the adversary (i.e., attacker) is assumedto violate the integrity and availability of a data-analytic system, while in PPML, the adversaryis assumed to violate the privacy and confidentiality of an ML system.

Most of the time, compromise in security is caused by the intentional attack by a thirdparty. We are concerned with three major types of attacks in ML.

• Integrity attack. An attack on integrity may result in intrusion points being classified asnormal (i.e., false negatives) by the ML system.

• Availability attack. An attack on availability may lead to classification errors (both falsenegatives and false positives) such that the ML system becomes unusable. This is a broadertype of integrity attacks.

• Confidentiality attack. An attack on confidentiality may result in sensitive information(e.g., training data or model) of an ML system being leaked.


Table 2.1 gives a comparison between PPML and secure ML in terms of security violations,adversary attacks, and defense techniques.



Table 2.1: Comparison between PPML and secure ML


<table><tr><td></td><td>Security Violations</td><td>Adversary Attacks</td><td>Defence Techniques</td></tr><tr><td rowspan="3">PPML</td><td rowspan="3">Privacy Confidentiality</td><td>Reconstruction attack</td><td>Secure multi-party computation</td></tr><tr><td>Inversion attack</td><td>Homomorphic encryption</td></tr><tr><td>Membership-inference attack</td><td>Differential privacy</td></tr><tr><td rowspan="3">Secure ML</td><td rowspan="3">Integrity Availability</td><td>Poisoning attack</td><td>Defensive distillation</td></tr><tr><td>Adversarial attack</td><td>Adversarial training</td></tr><tr><td>Oracle attack</td><td>Regularization</td></tr></table>

In this chapter, we mainly focus on PPML and defense techniques against privacy andconfidentiality violations in ML. Interested readers can refer to Barreno et al. [2006] for a moredetailed explanation of secure ML.

# 2.3 THREAT AND SECURITY MODELS

# 2.3.1 PRIVACY THREAT MODELS

In order to preserve privacy and confidentiality in ML, it is important to understand the possiblethreat models. In ML tasks, the participants usually take up three different roles: (1) as the inputparty, e.g., the data owner; (2) as the computation party (e.g., the model builder and inferenceservice provider); and (3) as the result party (e.g., the model querier and user) [Bogdanov et al.,2014].

Attacks on ML may happen in any stage, including data publishing, model training, andmodel inference. Attribute-inference attacks can happen in the data publishing stage, where ad-versaries may attempt to de-anonymize or target data-record owners for malevolent purposes.The attacks during ML model training are called reconstruction attacks, where the computation

party aims to reconstruct the raw data of the data providers or to learn more information aboutthe data providers than what the model builders intend to reveal.

For federated learning, reconstruction attacks are the major privacy concerns. In the in-ference phase of ML models, an adversarial result party may conduct reconstruction attack, modelinversion attacks, or membership-inference attacks, using reverse engineering techniques to gainextra information about the model or raw training data.

Reconstruction Attacks. In reconstruction attacks, the adversary’s goal is to extract thetraining data or feature vectors of the training data during ML model training or model infer-ence. In centralized learning, raw data from different data parties are uploaded to the compu-tation party, which makes the data vulnerable to adversaries, such as a malicious computationparty. Large companies may collect raw data from users to train an ML model. However, thecollected data may be used for other purposes or sent to a third-party without informed consentfrom the users. In federated learning, each participating party carries out ML model trainingusing their local data. Only the model weight updates or gradient information are shared withother parties. However, the gradient information may also be leveraged to reveal extra informa-tion about the training data [Aono et al., 2018]. Plain-text gradient updating may also violateprivacy in some application scenarios. To resist reconstruction attacks, ML models that storeexplicit feature values such as support vector machine (SVM) and k-nearest neighbors (kNN)should be avoided. During model training, secure multi-party computation (MPC) [Yao, 1982]and homomorphic encryption (HE) [Rivest et al., 1978] can be used to defend against suchattacks by keeping the intermediate values private. During model inference, the party comput-ing the inference result should only be granted black-box access to the model. MPC and HEcan be leveraged to protect the privacy of the user query during model inference. MPC, HE,and their corresponding applications in PPML will be introduced in Sections 2.4.1 and 2.4.2,respectively.

Model Inversion Attacks. In model inversion attacks, the adversary is assumed to haveeither white-box access or black-box access to the model. For the case of white-box access,the adversary knows the clear-text model without stored feature vectors. For the case of black-box access, the adversary can only query the model with data and collect the responses. Theadversary’s target is to extract the training data or feature vectors of the training data fromthe model. The black-box access adversary may also reconstruct the clear-text model from theresponse by conducting an equation solving attack. Theoretically, for an $N$ -dimensional linearmodel, an adversary can steal it with $N + 1$ queries. Such a problem can be formalized as solving$\theta$ from $( x , h _ { \theta } ( x ) )$ . The adversary can also learn a similar model using the query-response pairsto simulate the original model. To resist model inversion attacks, less knowledge of the modelshould be exposed to the adversary. The access to model should be limited to black-box access,and the output should be limited as well. There are several strategies proposed to reduce thesuccess rate of model inversion attack. Fredrikson et al. [2015] choose to report only rounded

confidence values. Al-Rubaie and Chang [2016] take the predicted class labels as response, andthe aggregated prediction results of multiple testing instances are returned to further enhancemodel protection. Bayesian neural networks combined with homomorphic encryption have beendeveloped [Xie et al., 2019], to resist such attacks during secure neural network inference.

Membership-Inference Attacks. In membership-inference attacks, the adversary hasblack-box access to a model, as well as a certain sample, as its knowledge. The adversary’s targetis to learn if the sample is inside the training set of the model. The adversary infers whether asample belongs to the training set or not based on the ML model output. The adversary con-ducts such attacks by finding and leveraging the differences in the model predictions on thesamples belonging to the training set vs. other samples. Defense techniques that are proposedto resist model inversion attacks, such as result generalization by reporting rounded predictionresults are shown to be effective to thwart such attacks [Shokri et al., 2017]. Differential privacy(DP) [Dwork et al., 2006] is a major approach to resist membership inference attacks, whichwill be introduced in Section 2.4.3.

Attribute-Inference Attacks. In attribute-inference attacks, the adversary tries to de-anonymize or target record owners for malevolent purpose. Anonymization by removing per-sonally identifiable information (PII) (also known as sensitive features), such as user IDs andnames, before data publishing appears to be a natural approach for protecting user privacy. How-ever, it has been shown to be ineffective. For example, Netflix, the world’s largest online movierental service provider, released a movie rating dataset, which contains anonymous movie ratingsfrom 500,000 subscribers. Despite anonymization, Narayanan and Shmatikov [2008] managedto leverage this dataset along with the Internet Movie Database (IMDB) as background knowl-edge to re-identify the Netflix users in the records, and further managed to deduce the user’sapparent political preferences. This incident shows that anonymization fails in the face of strongadversaries with access to alternative background knowledge. To deal with attribute-inferenceattacks, group anonymization privacy approaches have been proposed in Mendes and Vilela[2017]. Privacy preservation in group anonymization privacy is achieved via generalization andsuppression mechanisms.

Model Poisoning Attacks. It has been shown that federated learning may be vulnerableto model poisoning attacks [Bhagoji et al., 2019], also known as backdoor attacks [Bagdasaryanet al., 2019]. For example, a malicious participant in federated learning may inject a hiddenbackdoor functionality into the trained federated model, e.g., to cause a trained word predictorto complete certain sentences with an attacker-chosen word [Bagdasaryan et al., 2019]. Bhagojiet al. [2019] proposed a number of strategies to carry out model poisoning attacks, such asboosting of the malicious participant’s model update, an alternating minimization strategy thatalternately optimizes for the legit training loss and the adversarial backdoor objective, and usingparameter estimation for the benign updates to improve attack success. Bagdasaryan et al. [2019]developed a new model-poisoning methodology using model replacement, where a constrain-

and-scale technique is proposed to evade anomaly detection-based defenses by incorporating theevasion into the attacker’s loss function during model training. Possible solutions against modelpoisoning attacks include blockchain-based approaches [Preuveneers et al., 2018] and trustedexecution environment (TEE) based approaches [Mo and Haddadi, 2019].

# 2.3.2 ADVERSARY AND SECURITY MODELS

For cryptographic PPML techniques, including MPC and HE, two types of adversaries areconcerned in the literature.

• Semi-honest adversaries. In the semi-honest (a.k.a honest-but-curious, and passive) ad-versary model, the adversaries abide by the protocol honestly, but also attempt to learnmore information beyond the output from the received information.

• Malicious adversaries. In the malicious (a.k.a. active) adversary model, the adversariesdeviate from the protocol and can behave arbitrarily.

The semi-honest adversary model is widely considered in most PPML studies. The main reasonis that, in federated learning, it is beneficial to each party to honestly follow the ML protocol,since malicious behaviors also break the benefits of the adversaries themselves. The other reasonis that, in cryptography, it is a standard method to build a protocol secure against semi-honestadversaries first, then modify it to be secure against malicious adversaries via zero-knowledgeproof.

For both security models, the adversaries corrupt a fraction of the parties, and the cor-rupted parties may collude with each other. The corruption of parties can be static or adaptive.The complexity of an adversary can be either polynomial-time or computational unbounded,corresponding to information-theoretic secure and computational secure, respectively. The se-curity in cryptography is based on the notion of indistinguishability. Interested readers can referto Lindell [2005] and Lindell and Pinkas [2009] for detailed analysis of adversary and securitymodels.

# 2.4 PRIVACY PRESERVATION TECHNIQUES

In this section, we discuss privacy preservation techniques. We cover three types of such ap-proaches, namely (1) MPC, (2) HE, and (3) DP.

# 2.4.1 SECURE MULTI-PARTY COMPUTATION

Secure Multi-Party Computation (MPC), a.k.a. secure function evaluation (SFE), was initiallyintroduced as a secure two-party computation problem (the famous Millionaire’s Problem), andgeneralized in 1986 by Andrew Yao [1986]. In MPC, the objective is to jointly compute afunction from the private input by each party, without revealing such inputs to the other parties.

MPC tells us that for any functionality, it is possible to compute it without revealing anythingother than the output.

# Definition

MPC allows us to compute functions of private input values so that each party learns onlythe corresponding function output value, but not input values from other parties. For example,given a secret value $x$ that is split into $n$ shares so that a party $P _ { i }$ only knows $x _ { i }$ , all parties cancollaboratively compute

$$
y _ {1}, \dots , y _ {n} = f (x _ {1}, \dots , x _ {n})
$$

so that party $P _ { i }$ learns nothing beyond the output value $y _ { i }$ corresponding to its own input $x _ { i }$

The standard approach to prove that an MPC protocol is secure is the simulationparadigm [Lindell, 2017]. To prove an MPC protocol is secure against adversaries that cor-rupt $t$ parties under the simulation paradigm, we build a simulator that, when given inputs andoutputs of t colluding parties, generates t transcripts, so that the generated transcripts are indis-tinguishable to that generated in the actual protocol.

In general, MPC can be implemented through three different frameworks, namely:(1) Oblivious Transfer (OT) [Keller et al., 2016, Goldreich et al., 1987]; (2) Secret Sharing(SS) [Shamir, 1979, Rabin and Ben-Or, 1989]; and (3) Threshold Homomorphic Encryption(THE) [Cramer et al., 2001, Damgård and Nielsen, 2003]. From a certain point of view, bothoblivious transfer protocols and threshold homomorphic encryption schemes use the idea of se-cret sharing. This might be the reason why secret sharing is widely regarded as the core of MPC.In the rest of this section, we will introduce oblivious transfer and secret sharing.

# Oblivious Transfer

OT is a two-party computation protocol proposed by Rabin in 1981 [Rabin, 2005]. In OT,the sender owns a database of message-index pairs $( M _ { 1 } , 1 ) , \ldots , ( M _ { N } , N )$ . At each transfer, thereceiver chooses an index $i$ for some $1 \leq i \leq N$ , and receives $M _ { i }$ . The receiver does not learnany other information about the database, and the sender does not learn anything about thereceiver’s selection i. Here, we give the definition of 1-out-of-n OT.

Definition 2.1 1-out-of-n OT: Suppose Party A has a list $( x _ { 1 } , \ldots , x _ { n } )$ as the input, Party Bhas $i \in { 1 , \dots , n }$ as the input. 1-out-of-n OT is an MPC protocol where A learns nothing about$i$ and B learns nothing else but $x _ { i }$ .

When $n = 2$ , we get 1-out-of-2 OT which has the following property: 1-out-of-2 OT isuniversal for two-party MPC [Ishai et al., 2008]. That is, given a 1-out-of-2 OT protocol, onecan conduct any secure two-party computation.

Many Constructions of OT has been proposed such as Bellare–Micali’s [Bellare and Mi-cali, 1990], Naor–Pinka’s [Naor and Pinkas, 2001], and Hazay–Lindell’s [Hazay and Lindell,

2010] approaches. Here, we demonstrate the Bellare-Micali’s construction of OT, which uti-lizes Diffie–Hellman key exchange and is based on the computational Diffie–Hellman (CDH)assumption [Diffie and Hellman, 1976]. The Bellare–Micali’s construction works as follows:the receiver sends two public keys to the sender. The receiver only holds one private key corre-sponding to one of the two public keys, and the sender does not know which public key it is.Then, the sender encrypts the two massages with their corresponding public keys, and sends theciphertexts to the receiver. Finally, the receiver decrypts the target ciphertext with the privatekey.

Bellare–Micali Construction. In a discrete logarithm setting $( \mathbb { G } , g , p )$ , where $\mathbb { G }$ is agroup of prime order $p , g \in \mathbb { G }$ is a generator, and ${ \cal H } : { \cal G }  \{ 0 , 1 \} ^ { n }$ is a hash function. Supposethe sender A has $x _ { 0 } , x _ { 1 } \in \{ 0 , 1 \} ^ { n }$ , and the receiver B has $b \in \{ 0 , 1 \}$ .

1. A chooses a random element $c  G$ and sends it to B.

2. B chooses $k  \mathbb { Z } _ { p }$ and sets $P K _ { b } = g ^ { k }$ , $P K _ { 1 - b } = c / P K _ { b }$ , then sends $P K _ { 0 }$ to A. A sets$P K _ { 1 } = c / P K _ { 0 }$ .

3. A encrypts $x _ { 0 }$ with ElGamal scheme using $P K _ { 0 }$ (i.e., setting $C _ { 0 } = [ g ^ { r _ { 0 } } , H A S H ( P K _ { 0 } ^ { r _ { 0 } } ) * x _ { 0 } ]$and encrypting $x _ { 1 }$ using $P K _ { 1 }$ ). Then, A sends $( C _ { 0 } , C _ { 1 } )$ to B.

4. B decrypts $C _ { b }$ using private key $k$ to obtain $x _ { b } = P K _ { b } ^ { r _ { b } } * x _ { b } / g ^ { r _ { b } k }$

Yao’s Garbled Circuit (GC). [Yao, 1986] is a well-known OT-based secure two-partycomputation protocol that can evaluate any function. The key idea of Yao’s GC is to decomposethe computational circuits into generation and evaluation stages. The circuits consisting of gateslike AND, OR, and NOT can be used to compute any arithmetic operation. Each party isin charge of one stage and the circuit is garbled in each stage, so that any of them cannot getinformation from the other one, but they can still achieve the result according to the circuit. GCconsists of an OT protocol and a block cipher. The complexity of the circuit grows at least linearlywith the input size. Soon after GC was proposed, GMW [Goldreich et al., 1987] extended GCto the multi-party setting against malicious adversaries. For more detailed survey of GC, readerscan refer to Yakoubov [2017].

OT Extension. Impagliazzo and Rudich [1989] showed that OT provably requires“public-key” type of assumptions (such as factoring, discrete log, etc.). However, Beaver [1996]pointed out that OT can be “extended” in the sense that it is enough to generate a few “seed”OTs based on public-key cryptography, which can then be extended to any number of OTsusing symmetric-key cryptosystems only. OT extension is now widely applied in MPC proto-cols [Keller et al., 2016, Mohassel and Zhang, 2017, Demmler et al., 2015] to improve efficiency.

# Secret Sharing

Secret sharing is a concept of hiding a secret value by splitting it into random parts and dis-tributing these parts (a.k.a. shares) to different parties, so that each party has only one share andthus only one piece of the secret [Shamir, 1979, Beimel, 2011]. Depending on the specific secretsharing schemes used, all or a known threshold of shares are needed to reconstruct the originalsecret value [Shamir, 1979, Tutdere and Uzunko, 2015]. For example, Shamir’s Secret Sharingis constructed based on polynomial equations and provides information-theoretic security, andit is also efficient using matrix calculation speedup [Shamir, 1979]. There are several types ofsecret sharing, mainly including arithmetic secret sharing [Damård et al., 2011], Shamir’s se-cret sharing [Shamir, 1979], and binary secret sharing [Wang et al., 2007]. As arithmetic secretsharing is mostly adopted by existing SMPC-based PPML approaches and binary secret sharingare closely related to OT which is discussed in Section 2.4.1, here we focus on arithmetic secretsharing.

Consider that a party $P _ { i }$ wants to share a secret $S$ among n parties $\{ P _ { i } \} _ { i = 1 } ^ { n }$ in a finitefield $F _ { q }$ . To share $S$ , the party $P _ { i }$ randomly samples $n - 1$ values $\{ s _ { i } \} _ { i = 1 } ^ { n - 1 }$ from $\mathbb { Z } _ { q }$ D and set $s _ { n } =$$\textstyle S - \sum _ { i = 1 } ^ { \bar { n } - 1 } s _ { i }$ mod $q$ . Then, $P _ { i }$ distributes $s _ { k }$ to party $P _ { k }$ , for $k \neq i$ iD1 . We denote the shared $S$ as$\langle S \rangle = \{ s _ { i } \} _ { i = 1 } ^ { n }$ .

The arithmetic addition operation is carried out locally at each party. The secure multipli-cation is performed by using Beaver triples [Beaver, 1991]. The Beaver triples can be generatedin an offline phase. The offline phase (i.e., preprocessing) serves as a trusted dealer who generatesBeaver triples $\{ ( \langle a \rangle , \langle b \rangle , \langle c \rangle ) | a b = c \}$ and distributes the shares among the $n$ parties.

To compute $\langle z \rangle = \langle x \rangle \cdot \langle y \rangle = \langle x * y \rangle$ , $P _ { i } { _ { i = 1 } ^ { n } }$ first computes $\left. e \right. = \left. x \right. - \left. a \right.$ , $\langle f \rangle = \langle y \rangle -$$\left. b \right.$ . Then, $e$ and $f$ are reconstructed. Finally, $P _ { i }$ computes $\langle z \rangle = \langle c \rangle + e \langle x \rangle + f \langle y \rangle$ locally, anda random party $P _ { j }$ adds its share into $e f$ . We denote element-wise multiplication of vectors as$\langle \cdot \rangle \odot \langle \cdot \rangle$ .

Secure multiplication can also be performed by leveraging the Gilboa’s protocol [Gilboa,1999], in which $n$ -bit arithmetic multiplication can be conducted via n 1-out-of-2 OTs. Supposethat Party A holds $x$ and Party B holds $y$ . Now we show Gilboa’s protocol, which results in Aholding $\langle z \rangle _ { A }$ and B holding $\langle z \rangle _ { B }$ such that $z = x \cdot y$ . Let l be the maximum length of the binaryrepresentation of the numbers involved in our protocol. Denote the $m \times 1$ -out-of-2 OT for $l$ -bitstrings as $O T _ { l } ^ { m }$ . Denote the ith bit of $x$ as $x [ i ]$ . The secure 2-party multiplication via OT can beconducted as follows.

1. A represents $x$ in binary format.

2. B builds $O T _ { l } ^ { l }$ . For the ith OT, randomly pick $a _ { i , 0 }$ and compute $a _ { i , 1 } = 2 ^ { i } y - a _ { i , 0 }$ . Use$( - a _ { i , 0 } , a _ { i , 1 } )$ as the input for the ith OT.

3. A inputs $\mathrm { X } [ i ]$ as the choice bit in the ith OT and obtains $\mathrm { x } [ i ] \times 2 ^ { i } y - a _ { i , 0 }$

4. A computes $\begin{array} { r } { \langle z \rangle _ { A } = \sum _ { i = 1 } ^ { l } ( x [ i ] \times 2 ^ { i } y - a _ { i , 0 } ) } \end{array}$

B computes $\begin{array} { r } { \langle z \rangle _ { B } = \sum _ { i = 1 } ^ { l } a _ { i , 0 } } \end{array}$

The offline phase can be carried out efficiently with the help of a semi-honest dealerwho generates Beaver triples and distributes them among all the parties. To perform such apreprocessing step without a semi-honest dealer, there are several protocols available, such asSPDZ [Damård et al., 2011], SPDZ-2 [Damård et al., 2012], MASCOT [Keller et al., 2016],and HighGear [Keller et al., 2018].

• SPDZ is an offline protocol in the preprocessing model based on somewhat homomorphicencryption (SHE) in the form of BGV, first described in Damård et al. [2011].

• SPDZ-2 [Damård et al., 2012] is a protocol based on threshold SHE cryptography (witha shared decryption key).

• MASCOT is an oblivious-transfer-based protocol, proposed in Keller et al. [2016]. It isfar more computationally efficient than SPDZ and SPDZ-2.

• In 2018, Keller et al. [2018] developed a BGV-based SHE protocol, called the HighGearprotocol, which achieves better performance than the MASCOT protocol.

# Application in PPML

Various MPC-based approaches have been designed and implemented for PPML in the past.Most MPC-based PPML approaches leverage a two-phase architecture, comprising of an offlinephase and an online phase. The majority of cryptographic operations are conducted in the offlinephase, where multiplication triples are generated. The ML model is then trained in the onlinephase using the multiplication triples generated in the offline phase. The DeepSecure [Rouhaniet al., 2017] is a GC-based framework for secure neural network inference, where the inferencefunction has to be represented as a Boolean circuit. The computation and communication costin GC only depend on the total number of AND gates in the circuit.

SecureML [Mohassel and Zhang, 2017] is another two-party framework for PPML em-ploying two-phase architecture. Parties in federated learning distributes arithmetic shared oftheir data among two non-colluding servers, who run secure two-party model training proto-cols. Both Linearly HE (LHE)-based and OT-based protocols are proposed for multiplicationtriples generation in offline phase. The online phase is based on arithmetic secret sharing anddivision GC. Therefore, only linear operations are allowed in model training, and various ap-proximations are done to nonlinear functions.

The Chameleon framework is another hybrid MPC framework based on ABY for neuralnetwork model inference [Demmler et al., 2015]. Arithmetic secret sharing is used to conductlinear operations, and GC as well as GMW [Goldreich et al., 1987] are used for nonlinearoperations. Conversion protocols are also implemented to convert data representations amongdifferent protocols.

Privacy-preserving ID3 learning based on OT is addressed in Lindell and Pinkas [2002].Shamir’s threshold secret sharing is used for secure model aggregation for PPML with secu-rity against both honest-but-curious and malicious adversaries [Bonawitz et al., 2017], where a

group of clients do MPC to evaluate the average of their private input models, and disclose theaverage to the parameter server for model update. Recently, MPC-based approaches pursuingsecurity against malicious corrupted majority has been studied. For example, linear regressionand logistic regression training and evaluation with SPDZ is studied in Chen et al. [2019].The authors in Damgård et al. [2019] embraces $\mathrm { S P D } Z _ { 2 ^ { \mathrm { k } } }$ [Cramer et al., 2018] for actively se-cure private ML against a dishonest majority. It implements decision tree and SVM evaluationalgorithms.

# 2.4.2 HOMOMORPHIC ENCRYPTION

HE is generally considered as an alternative approach to MPC in PPML. HE can also be usedto achieve MPC as discussed in Section 2.4.1. The concept of HE was proposed in 1978 byRivest et al. [1978] as a solution to perform computation over ciphertext without decrypting theciphertext. Since then, numerous attempts have been made by researchers all over the world todesign such homomorphic schemes.

The encryption system proposed by Goldwasser and Micali [1982] was a provably secureencryption scheme that reached a remarkable level of safety. It allows an additive operation overciphertext, but is able to encrypt only a single bit. Paillier [1999] proposed a provable securityencryption system that also allows an additive operation over ciphertext in 1999. It has beenwidely used in various applications. A few years later, in 2005, Boneh et al. [2005] invented asystem of provable security encryption, which allows unlimited number of additive operationsand one multiplicative operation. Gentry made a breakthrough in 2009 and proposed the firstHE scheme that supports both additive and multiplicative operations for unlimited number oftimes [Gentry, 2009].

# Definition

An HE scheme $\mathcal { H }$ is an encryption scheme that allows certain algebraic operations to be carriedout on the encrypted content, by applying an efficient operation to the corresponding ciphertext(without knowing the decryption key). An HE scheme $\mathcal { H }$ consists of a set of four functions:

$$
\mathcal {H} = \{K e y G e n, E n c, D e c, E v a l \}, \tag {2.1}
$$

where

- KeyGen: Key generation. A cryptographic generator $g$ is taken as the input. For asym-metric HE, a pair of keys $\{ p k , s k \} = K e y G e n ( g )$ are generated, where $p k$ is the publickey for encryption of the plaintext and $s k$ is the secret (private) key for decryption of theciphertext. For symmetric HE, only a secret key $s k = K e y G e n ( g )$ is generated.

- Enc: Encryption. For asymmetric HE, an encryption scheme takes the public key $p k$ andthe plaintext m as the input, and generates the ciphertext $c = E n c _ { p k } ( m )$ as the output. Forsymmetric HE, an HE scheme takes the secret key $s k$ and the plaintext $m$ , and generatesciphertext $c = E n c _ { s k } ( m )$ .

- Dec: Decryption. For both symmetric and asymmetric HE, the secret key $s k$ and theciphertext c are taken as the input to produce the corresponding plaintext $m = D e c _ { s k } ( c )$ .

- Eval: Evaluation. The function Eval takes the ciphertext $c$ and the public key $p k$ (forasymmetric HE) as the input, and outputs a ciphertext corresponding to a functionedplaintext.

Let $E n c _ { e n k } ( \cdot )$ denote the encryption function with enk as the encryption key. Let $\mathcal { M }$ de-note the plaintext space and $\mathcal { C }$ denote the ciphertext space. A secure cryptosystem is calledhomomorphic if it satisfies the following condition:

$$
\forall m _ {1}, m _ {2} \in \mathcal {M}, \operatorname {E n c} _ {\text {e n k}} \left(m _ {1} \odot_ {\mathcal {M}} m _ {2}\right) \leftarrow \operatorname {E n c} _ {\text {e n k}} \left(m _ {1}\right) \odot_ {\mathcal {C}} \operatorname {E n c} _ {\text {e n k}} \left(m _ {2}\right) \tag {2.2}
$$

for some operators $\odot _ { \mathcal { M } }$ in $\mathcal { M }$ and $\odot _ { } c$ in $\mathcal { C }$ , where indicates the left-hand side term is equal toor can be directly computed from the right-hand side term without any intermediate decryption.In this book we denote homomorphic encryption operator as ŒŒ, and we overload the additionand multiplication operators over ciphertexts as follows.

• Addition: $D e c _ { s k } ( [ [ u ] ] \odot _ { \mathcal { C } } [ [ v ] ] ) = D e c _ { s k } ( [ [ u + v ] ] )$ , where $^ { \mathfrak { s } } \textcircled { \cdot } { c } ^ { \mathfrak { n } }$ may represent multiplica-tion of the ciphertexts (see, e.g., Paillier [1999]).

• Scalar multiplication: $D e c _ { s k } ( [ [ u ] ] \odot _ { \mathcal { C } } n ) = D e c _ { s k } ( [ [ u \cdot n ] ] )$ , where $\ " \odot \ - c \ \ "$ may represent tak-ing the power of $n$ of the ciphertext (see, e.g., Paillier [1999]).

# Categorization of HE Schemes

HE schemes can be categorized into three classes: Partially Homomorphic Encryption (PHE),Somewhat Homomorphic Encryption (SHE), and Fully Homomorphic Encryption (FHE).In general, for HE schemes, the computational complexity increases as the functionality grows.Here, we provide a brief introduction to different types of HE schemes. Interested readers canrefer to Armknecht et al. [2015] and Acar et al. [2018] for more details regarding differentclasses of HE schemes.

Partially Homomorphic Encryption (PHE). For PHE, both $( \mathcal { M } , \odot _ { \mathcal { M } } )$ and $( \mathcal { C } , \odot _ { \mathcal { C } } )$ aregroups. The operator $\odot _ { \mathcal { C } }$ can be applied on ciphertexts for a unlimited number of times. PHE is agroup homomorphism technique. Specifically, if $\odot _ { \mathcal { M } }$ is addition operator, the scheme is additivelyhomomorphic, and if $\odot _ { \mathcal { M } }$ is a multiplication operator, we say that the scheme is multiplicativehomomorphic. The references Rivest et al. [1978] and ElGamal [1985] represent two typicalmultiplicative HE schemes. Examples of additive HE schemes can be found in Goldwasser andMicali [1982] and Paillier [1999].

Somewhat Homomorphic Encryption (SHE). An HE scheme is called SHE if someoperations (e.g., addition and multiplication) can be applied for only a limited number of times.Some literature also refer to the schemes supporting arbitrary operations while only some limited

circuits (e.g., the branching programs [Ishai and Paskin, 2007], garbled circuit [Yao, 1982]) asSHE. Examples are BV [Brakerski and Vaikuntanathan, 2011], BGN [Boneh et al., 2005],and IP [Ishai and Paskin, 2007]. SHE schemes introduce noise for security. Each operationon the ciphertext increases the noise of the output ciphertext, and multiplication is the maintechnique for increasing noise. When the noise exceeds an upper bound, decryption cannot beconducted correctly. This is the reason why most SHE schemes require a limited number oftimes of applying the operations.

Fully Homomorphic Encryption (FHE). FHE schemes allow both additive and multi-plicative operations with unlimited number of times over ciphertexts. It is worth noticing thatadditive and multiplicative operations are the only two operations needed to compute arbitraryfunctions. Consider $4 , B \in \mathbb { F } _ { 2 }$ . The NAND gate can be constructed by $1 + A * B$ . Thanks toits functional completeness, the NAND gate can be used to construct any gate. Therefore, anyfunctionality can be evaluated by FHE. There are four main families of FHE [Acar et al., 2018]:(1) Ideal Lattice-based FHE (see, e.g., Gentry [2009]); (2) Approximate-GCD based FHE (see,e.g., Dijk et al. [2010]); (3) (R)LWE-based FHE (e.g., Lyubashevsky et al. [2010] and Brakerskiet al. [2011]); and (4) NTRU-like FHE (see, e.g., López-Alt et al. [2012]).

The existing FHE schemes are built on SHE, by assuming circular security and imple-menting an expensive bootstrap operation. The bootstrap operation re-encrypts the ciphertexts,by evaluating the decryption and encryption functions over the ciphertexts and the encryptedsecret key, in order to reduce the noise of ciphertext for further computation. As a result ofthe costly bootstrap operation, FHE schemes are very slow and not competitive against gen-eral MPC approaches in practice. Researchers are now focusing on finding more efficient SHEschemes that satisfy certain requirements, instead of trying to develop an FHE scheme. In ad-dition, FHE schemes assume circular security (a.k.a. key dependent message (KDM) security),which keeps the secret key secure by encrypting it with the public key. However, no FHE isproven to be semantically secure with respect to any function and is IND-CCA1 secure [Acaret al., 2018].

# Application in PPML

Many research efforts based on HE have been devoted to PPML in the past. For example, Hardyet al. [2017] proposed algorithms for privacy-preserving two-party logistic regression for ver-tically partitioned data. Paillier’s scheme is leveraged in secure gradient descent to train thelogistic regression model, where constant-multiplication and addition operations are conductedvia a mask encrypted by Paillier’s scheme and the intermediate data computed by each party. Theencrypted masked intermediate results are exchanged between the two parties in the secure gra-dient descent algorithm. Finally, the encrypted gradient is sent to a coordinator for decryptionand model update.

CryptoNets [Gilad-Bachrach et al., 2016] is an HE-based methodology announced byMicrosoft Research that allows secure evaluation (inference) of encrypted queries over already

trained neural networks on cloud servers: queries from the clients can be classified securely bythe trained neural network model on a cloud server without inferring any information aboutthe query or the result. The CryptoDL [Hesamifard et al., 2017] framework is a leveled HE-based approach for secure neural network inference. In CryptoDL, several activation functionsare approximated using low-degree polynomials and mean-pooling is used as a replacementfor max-pooling. The GAZELLE [Juvekar et al., 2018] framework is proposed as a scalableand low-latency system for secure neural network inference. In GAZELLE, to conduct securenonlinear function evaluation in neural network inference, HE and traditional secure two-partycomputation techniques (such as GC) are combined in an intricate way. The packed additivehomomorphic encryption (PAHE) embraced in GAZELLE allows single instruction multipledata (SIMD) arithmetic homomorphic operations over encrypted data.

FedMF [Chai et al., 2019] uses Paillier’s HE for secure federated matrix factorizationassuming honest-but-curious server and honest clients. Secure federated transfer learning isstudied via Paillier’s HE scheme in Liu et al. [2019], where the semi-honest third party is intothe discard by mixing HE with additive secret sharing in decryption process.

# 2.4.3 DIFFERENTIAL PRIVACY

DP was originally developed to facilitate secure analysis over sensitive data. With the rise ofML, DP has become an active research field again in the ML community. This is motivatedby the fact that many exciting results from DP can be applied to PPML [Dwork et al., 2016,2006]. The key idea of DP is to confuse the adversaries when they are trying to query individualinformation from the database so that adversaries cannot distinguish individual-level sensitivityfrom the query result.

# Definition

DP is a privacy definition initially proposed by Dwork et al. [2006], developed in the contextof statistical disclosure control. It provides an information-theoretic security guarantee that theoutcome of a function to be insensitive to any particular record in the dataset. Therefore, DPcan be used to resist the membership inference attack. The $( \epsilon , \delta )$ -differential privacy is definedas follows.

Definition 2.2 $( \epsilon , \delta )$ -differential privacy. A randomized mechanism $\mathcal { M }$ preserves $( \epsilon , \delta )$ -differential privacy if given any two datasets $D$ and $D ^ { \prime }$ differing by only one record, and forall $S \subset R a n g e ( \mathcal { M } )$ ,

$$
\Pr [ \mathcal {M} (d) \in S ] \leq \Pr [ \mathcal {M} \left(D ^ {\prime}\right) \in S ] \times e ^ {\epsilon} + \delta , \tag {2.3}
$$

where $\epsilon$ is the privacy budget and $\boldsymbol { \delta }$ is the failure probability.

The quantity ln $\frac { \mathrm { P r } [ \mathcal { M } ( D ) \in S ] } { \mathrm { P r } [ \mathcal { M } ( D ^ { \prime } ) \in S ] }$ is called the privacy loss, with ln denoting natural logarithmoperation. When $\delta = 0$ , the stronger notion of $\epsilon$ -differential privacy is achieved.

DP has utility-privacy trade-offs as it introduces noise to data. Jayaraman and Evans[2019] found out that current mechanisms for differential privacy for ML rarely offer accept-able utility-privacy trade-offs: settings that provide limited accuracy loss provide little effectiveprivacy, and settings that provide strong privacy result in large accuracy loss.

# Categorization of DP Schemes

Typically, there are mainly two ways to achieve DP by adding noise to the data. One is theaddition of noise according to the sensitivity of a function [Dwork et al., 2006]. The other ischoosing noise according to an exponential distribution among discrete values [McSherry andTalwar, 2007].

The sensitivity of a real-valued function expresses the maximum possible change in itsvalue due to the addition or removal of a single sample.

Definition 2.3 Sensitivity. For two datasets $D$ and $D ^ { \prime }$ differing by only one record, and afunction $\mathcal { M } : \mathcal { D }  \mathcal { R } ^ { d }$ over an arbitrary domain, the sensitivity of $\mathcal { M }$ is the maximum changein the output of $\mathcal { M }$ over all possible inputs:

$$
\Delta \mathcal {M} = \max  _ {D, D ^ {\prime}} \| \mathcal {M} (D) - \mathcal {M} \left(D ^ {\prime}\right) \|, \tag {2.4}
$$

where $\left\| \cdot \right\|$ is a norm of the vector. The $l _ { 1 }$ -sensitivity or the $l _ { 2 }$ -sensitivity is defined when the$l _ { 1 }$ -norm or $l _ { 2 }$ -norm is applied, respectively.

We denote the Laplace distribution with parameter $b$ as Lap.b/. Lap.b/ has a probabilitydensity function $\begin{array} { r } { P ( z | b ) = \frac { 1 } { 2 b } \exp ( - | z | / b ) } \end{array}$ . Given a function $\mathcal { M }$ with sensitivity $\Delta \mathcal { M }$ , the addi-tion of noise drawn from a calibrated Laplace distribution $L a p ( \Delta \mathcal { M } / \epsilon )$ maintains $\epsilon$ -differentialprivacy [Dwork et al., 2006].

Theorem 2.4 Given a function $\mathcal { M } : \mathcal { D }  \mathcal { R } ^ { d }$ over an arbitrary domain $D$ , for any input $X$ , thefunction:

$$
\mathcal {M} (X) + \operatorname {L a p} \left(\frac {\Delta \mathcal {M}}{\epsilon}\right) ^ {d} \tag {2.5}
$$

provides -differential privacy. The -differential privacy can also be achieved by adding independentlygenerated Laplace noise from distribution $L a p ( \Delta \mathcal { M } / \epsilon )$ to each of the d output terms.

The addition of Gaussian or binomial noise, scaled to the $l _ { 2 }$ -sensitivity of the func-tion, sometimes yields better accuracy, while only ensuring the weaker $( \epsilon , \delta )$ -differential pri-vacy [Dwork et al., 2006, Dwork and Nissim, 2004].

The exponential mechanism [McSherry and Talwar, 2007] is another way to obtain DP. Theexponential mechanism is given a quality function $q$ that scores outcomes of a calculation, wherehigher scores are better. For a given database and $\epsilon$ parameter, the quality function induces a

probability distribution over the output domain, from which the exponential mechanism sam-ples the outcome. This probability distribution favors high-scoring outcomes, while ensuring$\epsilon$ -differential privacy.

Definition 2.5 Let $q : ( \mathcal { D } ^ { n } \times \mathcal { R } )  \mathbb { R }$ be a quality function, which given a dataset $d \in \mathcal { D } ^ { n }$ ,assigns a score to each outcome $r \in \mathcal { R }$ . For any two datasets $D$ and $D ^ { \prime }$ differing by only onerecord, let $S ( q ) = \operatorname* { m a x } _ { r , D , D ^ { \prime } } \| q ( D , r ) - q ( D ^ { \prime } , r ) \| _ { 1 } .$ Let $\mathcal { M }$ be a mechanism for choosing an outcome$r \in \mathcal { R }$ given a dataset instance $d \in D ^ { n }$ . Then, the mechanism $\mathcal { M }$ , defined as

$$
\mathcal {M} (d, q) = \left\{\text {r e t u r n} r \text {w i t h p r o b a b i l i t y} \propto \exp \left(\frac {\epsilon q (d , r)}{2 S (q)}\right) \right\} \tag {2.6}
$$

provides $\epsilon$ -differential privacy.

The DP algorithms can be categorized according to how and where the perturbation isapplied.

1. Input perturbation: The noise is added to the training data.

2. Objective perturbation: The noise is added to the objective function of the learning al-gorithms.

3. Algorithm perturbation: The noise is added to the intermediate values such as gradientsin iterative algorithms.

4. Output perturbation: The noise is added to the output parameters after training.

DP still exposes the statistics of a party, which are sensitive in some cases, such as financialdata, medical data and other commercial and health applications. Readers who are interested inDP and willing to learn more about it can refer to the tutorial given by Dwork and Roth [2014].

# Application in PPML

In federated learning, to enable model training on distributed datasets held by multiple parties,local differential privacy (LDP) can be used. With local differential privacy, each input partywould perturb their data, then release the obfuscated data to the un-trusted server. The mainidea behind local differential privacy is randomized response (RR).

Papernot et al. [2016] utilized the teacher ensemble framework to first learn a teachermodel ensemble from the distributed datasets among all the parties. Then, the teacher modelensemble is used to make noisy predictions on a public dataset. Finally, the labeled public datasetis used to train a student model. The privacy loss is precisely controlled by the number of publicdata samples inferred by the teacher ensemble. Generative adversarial network (GAN) is furtherapplied in Papernot et al. [2018] to generate synthetic training data for the training of the student

model. Although this approach is not limited to a single ML algorithm, it requires adequate dataquantity at each location.

Moments accountant is proposed for differentially private stochastic gradient descent(SGD), which computes the overall privacy cost in neural networks model training by takinginto account the particular noise distribution under consideration [Abadi et al., 2016]. It provesless privacy loss for appropriately chosen settings of the noise scale and the clipping threshold.

The differentially private Long Short Term Memory (LSTM) language model is builtwith user-level differential privacy guarantees with only a negligible cost in predictive accu-racy [McMahan et al., 2017]. Phan et al. [2017] proposed a private convolutional deep beliefnetwork (pCDBN) by leveraging the functional mechanism to perturb the energy-based objec-tive functions of traditional convolutional deep belief networks. Generating differentially privatedatasets using GANs is explored in Triastcyn and Faltings [2018], where a Gaussian noise layeris added to the discriminator of a GAN to make the output and the gradients differentiallyprivate with respect to the training data. Finally, the privacy-preserving artificial dataset is syn-thesized by the generator. In addition to the DP dataset publishing, differentially private modelpublishing for deep learning is also addressed in Yu et al. [2019], where concentrated DP and adynamic privacy budget allocator are embraced to improve the model accuracy.

Geyer et al. [2018] studied differentially private federated learning and proposed an algo-rithm for client-level DP preserving federated optimization. It was shown that DP on a clientlevel is feasible and high model accuracy can be reached when sufficiently many participants areinvolved in federated learning.

# Distributed Machine Learning

As we know from Chapter 1, federated learning and distributed machine learning (DML) shareseveral common features, e.g., both employing decentralized datasets and distributed train-ing. Federated learning is even regarded as a special type of DML by some researchers, see,e.g., Phong and Phuong [2019], Yu et al. [2018], Konecný et al. [2016b] and Li et al. [2019],or seen as the future and the next step of DML. In order to gain deeper insights into feder-ated learning, in this chapter, we provide an overview of DML, covering both the scalability-motivated and the privacy-motivated paradigms.

DML covers many aspects, including distributed storage of training data, distributed op-eration of computing tasks, and distributed serving of model results, etc. There exist a largevolume of survey papers, books, and book chapters on DML, such as Feunteun [2019], Ben-Nun and Hoefler [2018], Galakatos et al. [2018], Bekkerman et al. [2012], Liu et al. [2018],and Chen et al. [2017]. Hence, we do not intend to provide another comprehensive survey onthis topic. We focus here on the aspects of DML that are most relevant to federated learning,and refer the readers to the references for more details.

# 3.1 INTRODUCTION TO DML

# 3.1.1 THE DEFINITION OF DML

DML, also known as distributed learning, refers to multi-node machine learning (ML) or deeplearning (DL) algorithms and systems that are designed to improve performance, preserve pri-vacy, and scale to more training data and bigger models [Trask, 2019, Liu et al., 2017, Galakatoset al., 2018]. For example, as illustrated in Figure 3.1, a DML system with three workers (a.k.a.computing nodes) and one parameter server [Li et al., 2014], the training data are split into dis-joint data shards and sent to the workers, and the workers carry out stochastic gradient descent(SGD) at their locality. The workers send gradients $\triangle \mathbf { w } ^ { i }$ or model weights $\mathbf { w } ^ { i }$ to the parameterserver, where the gradients or model weights are aggregated (e.g., via taking weighted average)to obtain the global gradients w or model weights w. Both synchronous and asynchronousSGD algorithms can be applied in DML [Ben-Nun and Hoefler, 2018, Chen et al., 2017].

DML can generally be categorized into two classes, namely the scalability-motivatedDML and the privacy-motivated DML. The scalability-motivated DML refers to the DMLparadigm that is designed to address the ever-increasing scalability and computation require-ments of large-scale ML systems. For example, in the past decades, the scales of the problemsthat ML and DL methods have to deal with have increased exponentially. Training a sophisti-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/bbf6f1ebc30b6c443d3e7abf883ce47f691415dbb3b193f665eea9296fcc6f0c.jpg)



Figure 3.1: Illustration of a distributed machine learning (DML) system.


cated DL model with a huge amount of data can easily exceed the capability of the traditionalML paradigm that relies on a single computing entity. One outstanding example is the famousBERT model [Devlin et al., 2019], which requires multiple tensor processing units (TPUs) forpre-training and it may take several days even with a fleet of TPUs. To cope with such scenarios,the fast-developing DML methods are considered as the answer to the ever-increasing size andcomplexity of ML models.

Scalability-motivated DML approaches provide feasible solutions to large-scale ML sys-tems when memory limitation and algorithm complexity are the main obstacles. Besides over-coming the problem of requiring centralized storage of training data, DML system can havemore elastic and scalable computing resources, such as adding more computing entities on-demand. This is particularly helpful in the age of cloud computing, where we can ask for moreprocessors (such as CPUs, GPUs, or even TPUs) and memory in an on-demand manner. Inlight of this feature, the scalability-motivated DML is widely applied in the scenarios withhorizontally partitioned datasets, where disjoint subsets of training data are stored at differentcomputing entities.

Different from the scalability-motivated DML, the primary goal of privacy-motivatedDML paradigm is to preserve user privacy. As user privacy and data security become a globalconcern (see also Chapter 1 and Appendix A) [Mancuso et al., 2019], privacy-preserving MLis becoming a new trend in the ML community (see also Chapter 2) [Yang et al., 2019]. Ina privacy-motivated DML system, there are multiple parties and each of them holds a subset

of the training data. Due to privacy concerns, the parties do not wish to expose their data toeach other. Thus, distributed learning schemes are required to make use of the data of eachparticipating party to collaboratively train an ML model. The datasets held by different partiesmay have different attributes, resulting in the so-called vertical partition of training data. Thatis to say, privacy-motivated DML is often applied in the scenarios with vertically partitioneddatasets, with subsets of training data with different attributes held by different parties.

# 3.1.2 DML PLATFORMS

Because of the distributed and parallel computing architecture of DML, specialized ML plat-forms are required in order to reap the benefits of DML. There exist numerous commercial andopen-source DML platforms. We introduce here some of the representative frameworks.

One of the most widely used distributed data processing systems for ML is Apache SparkMLlib [Apache MLlib, 2019]. MLlib is Apache Spark’s scalable ML library. It is a memory-based DML framework and makes practical ML systems scalable and easy to deploy. MLliboffers distributed implementations of the conventional ML algorithms (as compared to DL),such as classification, regression, and clustering, etc. Apache DeepSpark offers implementationof distributed training framework for DL [DeepSpark, 2019].

Graph-based parallel processing is a relatively new approach for DML, which is also calledgraph parallelism in the context of DML (see Section 3.2.2). The platform GraphLab [Turi-Create, 2019, Low et al., 2010] offers scalable ML toolkits and implements fundamental algo-rithms like SGD and gradient descent with superior performance. Another graph parallelism-based computation platform is the Apache Spark GraphX, a new component in Spark, whichimplements a Pregel-like bulk-synchronous message passing application programming interface(API) [Apache GraphX, 2019], and Pregel is the parallel graph processing libraries from Googlethat is based on the Bulk Synchronous Processing (BSP) model [Malewicz et al., 2010].

The Distributed ML Toolkit (DMTK) released by Microsoft contains both algorithmicand system innovations [DMTK, 2019]. DMTK supports a unified interface for data paral-lelization, a hybrid data structure for big model storage, model scheduling for big model training,and automatic pipelining for high training efficiency.

DL requires training deep neural networks (DNNs) with massive number of parameterson a huge amount of data. Distributed and parallel computing is a perfect tool to take fulladvantage of the modern hardware. As for distributed DL, in addition to Apache DeepSpark,the popular DL frameworks, such as TensorFlow and PyTorch, all support distributed trainingand deployment.

TensorFlow supports distributed training of DNNs via tf.distribute, e.g., (i) allowing por-tions of the graph to be computed on different processes or even on different servers, and (ii) em-ploying multiple processors or even servers to train the same model over different slices of inputdatasets [Distributed TensorFlow, 2019]. TensorFlow offers the possibility to split big modelsover many devices, carrying out the training in parallel on different devices if the models are too

large to fit in the memory of a single device. In addition, this can be used to distribute compu-tation to servers with powerful GPUs, and have other computations done on servers with morememory. With distributed TensorFlow, we can scale up distributed model training to hundredsof GPUs. We can massively reduce the experimentation (e.g., hyper-parameter tuning) time byrunning many experiments in parallel on many GPUs and servers.

The distributed package included in PyTorch (i.e., torch.distributed) enables researchersand practitioners to easily parallelize their computations across processes and clusters of ma-chines [Arnold, 2019]. Similar to TensorFlow, distributed PyTorch allows a model to be logi-cally split into several parts (i.e., some layers in one part and some in others), then placing themon different computing devices. PyTorch leverages the message passing semantics and allowseach process to communicate data to any of the other processes. As opposed to the multiprocess-ing (e.g., torch.multiprocessing) package, processes in PyTorch can use different communicationbackends and are not restricted to being executed on the same machine.

# 3.2 SCALABILITY-MOTIVATED DML

In this section, we provide a brief review of the existing works on scalability-motivated DMLmethods. Readers are referred to Feunteun [2019], Ben-Nun and Hoefler [2018], Galakatos etal. [2018] and Bekkerman et al. [2012] for comprehensive surveys of DML schemes and thereferences therein for more technical details.

# 3.2.1 LARGE-SCALE MACHINE LEARNING

With the emergence of widespread communication and sensing devices, such as smartphones,portable gadgets, IoT sensors, and wireless cameras, data are ubiquitously available in enormousvolumes. In this big data era, the bottleneck of ML methods has shifted from being able to inferfrom small training samples to dealing with large-scale high-dimensional datasets. With thistrend shift, the ML community is faced with the challenge that the computation power and timedo not scale well with the dataset size, making it impossible to learn from large-scale trainingsamples with reasonable computation effort and time. We summarize in the following the majorchallenges that conventional ML methods are faced with when dealing with large-scale datasets.

1. Memory shortage. Conventional ML methods operate with the training samples entirelyin one main memory. Therefore, if the computational complexity of the training samplesexceed the main memory, the following problems may arise: (i) the trained model may notconverge or may result in poor performance (such as bad precision or recall), and (ii) inthe worst-case scenario, the ML models cannot be trained due to memory shortage.

2. Unreasonable training time. Some optimization process in ML algorithms may not scalewell with respect to the training samples, such as Gaussian Mixture Model (GMM) andpolynomial regression. As a result, when dealing with large-scale training samples, the timeconsumed by the training process may be too long for practical use. On top of training,

tuning hyper-parameters of ML models also takes a lot of time as we may need to try manydifferent settings. Hence, if the training process takes too long, hyper-parameters tuningcannot be performed effectively, which may result in poor ML models.

Distributed ML algorithms are part of large-scale learning algorithms which has receivedconsiderable attention over the last few years, thanks to its ability to distribute the learningprocess onto several devices to scale up learning algorithms. Recent advances on DML makeML tasks on big data feasible, scalable, flexible, and more efficient.

# 3.2.2 SCALABILITY-ORIENTED DML SCHEMES

Excessive research efforts have been cast on presenting effective frameworks and methods fordealing with large-scale datasets and ML models. Particularly, training large-scale DL mod-els is very time-consuming, with the training period ranging from days to even weeks. Morerecently, numerous research works have been carried out to push the frontiers of DML, aim-ing to reduce training time and cope with large-scale DL models. We review here some of thepopular scalability-oriented DML schemes, covering data parallelism, model parallelism, graphparallelism, task parallelism, hybrid parallelism, and mixed parallelism.

# Data Parallelism

The first instinct around DML is partitioning the training data into subsets, which are puton multiple computing entities that train the same model in parallel. This is known as the dataparallelism approach, also known as the data-centric approach [Jia et al., 2019, Das, 2019, Wang,2016]. In other words, data parallelism refers to processing multiple pieces (technically calledshards) of training data through multiple replicas of the same model with different computingdevices and communicating model information periodically. This approach can naturally scaleup well with increasing amounts of training data. However, as a replica of the model (e.g., anentire DNN) has to reside on a single device, it cannot deal with ML models with high memoryfootprints.

There are mainly two common approaches for data parallelism-based distributed training,namely synchronous training and asynchronous training. With synchronous training, all com-puting entities train on replicas of the same model over different slices of the training data insynchronization, and the gradients (or model weights) produced by the computing entities areaggregated after each training step carried out by the entities. With asynchronous training, allentities independently train replicas of the same model over subsets of the training data and up-date model weights or gradients asynchronously. Typically, synchronous training is supportedby the AllReduce architecture [Apache MapReduce, 2019, Fukuda, 2019], and asynchronoustraining by the parameter server architecture [Li et al., 2014].

Data parallelism can be used in the case that the training data is too large to be storedin a single device or to achieve faster training with parallel computing. Much work has beenconducted for training DL models with distributed data. For example, the distributed frame-

works, including DistBelief (which was later integrated into TensorFlow) from Google [Deanet al., 2012] and Project Adams [Chilimbi et al., 2014] from Microsoft, tend to train large-scalemodels with thousands of processors by utilizing both data and model parallelism.

# Model Parallelism

As DL models are getting larger and larger, e.g., the BERT model [Devlin et al., 2019], we mayface the problem that a DNN model cannot be loaded into the memory of a single computingentity. In such scenarios, we need to split the model and put parts of the model into differententities. This is called the model parallelism approach, also known as the model-centric ap-proach [Jia et al., 2019, Das, 2019, Wang, 2016]. In other words, model parallelism refers to thecase that a model (e.g., a DNN model) is being logically split into several parts (i.e., some layersin one part and some layers in other parts for a DNN model), then placing them in differentcomputing devices. Although doing so does reduce execution time (asynchronous processing ofdata), it is usually employed to address memory constraints. Models with a very large number ofparameters, which are difficult to fit into a single system due to high memory footprint, benefitfrom this type of strategy. For example, a single layer of a large DNN model can be fit intothe memory of a single device and forward and backward propagation involves communicationof output from one device to another in a serial fashion. We usually resort to model parallelismonly if the model cannot fit into a single machine, not primarily to speed up the training process.

Existing works on model parallelism-based distributed training are extensive. One out-standing example is AMPNet, studied in Gaunt et al. [2018]. AMPNet was implemented onmulti-core CPUs and it was shown that AMPnet training converged to the same accuracy asconventional synchronous training algorithms in a similar number of epochs, but took signifi-cantly shorter overall training time. A more recent example is OptCNN [Jia et al., 2018], whichuses layer-wise parallelism for parallelizing convolutional neural networks (CNNs) with linearcomputation graphs. OptCNN allows each layer in a CNN to use an individual parallelizationstrategy. It was shown in Jia et al. [2018] that layer-wise parallelism outperforms state-of-the-artapproaches by increasing training throughput, reducing communication costs, achieving betterscalability to multiple GPUs, while maintaining original model accuracy.

Earlier exemplary works on model parallelism include Dean et al. [2012] and Kim etal. [2016], and Jia et al. [2019]. Particularly, in Dean et al. [2012], Google presented down-pour SGD, which provides an asynchronous and distributed implementation of SGD. Down-pour SGD combines data parallelism and model parallelism, which divides training samplesamong different machines, and each machine has a unique copy of the whole/partial network.DeepSpark was first proposed in Kim et al. [2016]. It allows distributed execution of both Caffeand Google’s TensorFlow DL jobs on an Apache Spark cluster of machines [DeepSpark, 2019].DeepSpark makes deploying large-scale parallel and distributed DL easy and intuitive for prac-titioners.

# Graph Parallelism

As graph-based ML algorithms are fast-growing [Zhang et al., 2018], graph parallelism basedDML approaches are also receiving more attention. Graph parallelism, also known as thegraph-centric approach, is a relatively new technique to partition and distribute training dataand execute ML algorithms that is orders of magnitude faster than data parallelism-based ap-proaches [Tian et al., 2018, Wang, 2016, Low et al., 2010].

GraphLab, first studied in Low et al. [2010] as an improvement upon abstractions likeMapReduce, implements asynchronous iterative algorithms with sparse computational depen-dencies while ensuring data consistency. It achieves a high degree of parallel performance.GraphLab is able to achieve excellent parallel performance on large scale real-world ML tasks.

More recently, Xiao et al. [2017] proposed a new distributed graph engine called TUX2.TUX2 is intentionally optimized for DML to support heterogeneity, with a Stale SynchronousParallel model, and a new MEGA (Mini-batch, Exchange, GlobalSync, and Apply) model.TUX2 puts forward the convergence of graph computation and DML, with a flexible graphmodel to express ML algorithms efficiently. Advances in graph computation and DML willallow more ML algorithms and optimization to be expressed and implemented easily and effi-ciently at scale.

# Task Parallelism

Task parallelism, also known as the task-centric approach, covers the execution of computerprograms across multiple processors on the same or multiple machines. It focuses on executingdifferent operations in parallel to fully utilize the available computing resources in the form ofprocessors and memory. One example of task parallelism would be an application of creatingthreads for doing parallel processing where each thread is responsible for performing a differ-ent operation. Examples of the big data frameworks that utilize task parallelism are ApacheStorm [Apache Storm, 2019] and Apache YARN [Apache YARN, 2019].

It is common to combine task parallelism and data parallelism for DML. One outstandingexample is Boehm et al. [2016], which presented a systematic approach for combining taskparallelism and data parallelism for large-scale ML on top of MapReduce [Apache MapReduce,2019]. The proposed framework enables users to specify task- and data-parallel ML algorithmsin an easy and flexible way via a high-level primitive. The combined task and data parallelism ontop of MapReduce opens ways to share cluster resources with other MapReduce based systemssince the MapReduce scheduler provides global scheduling.

# Hybrid Parallelism and Mixed Parallelism

In practical implementations of DML systems, we often need to combine different types of par-allelism methods, resulting in the so-called hybrid parallelism, such as Apache YARN [ApacheYARN, 2019] and SystemML [Pansare et al., 2018, Boehm et al., 2016] for both data and taskparallelism. In fact, it is very common in practice to use both data and model parallelism simulta-

neously, such as Google downpour SGD [Dean et al., 2012] and the distributed DL frameworkproposed in Shrivastava et al. [2017]. Wang et al. [2018] to unify data, model, and hybrid par-allelism via tensor tiling. The SOYBEAN system proposed in Wang et al. [2018] is a hybridbetween data parallelism and model parallelism, and it performs automatic parallelization.

Under the broader umbrella of hybrid parallelism, there is also mixed parallelism, such asthe work of Krizhevsky [2014] and Song et al. [2019]. This kind of parallelism is sometimesadopted for training large-scale DNNs, by distributing some layers using data parallelism andother layers using model parallelism. Readers are referred to Wang et al. [2018] and Song et al.[2019] for more information and related works on hybrid parallelism and mixed parallelism.

# 3.3 PRIVACY-MOTIVATED DML

The DML system can not only accelerate the computing of large-scale data, but also integratedata from different sites. In many practical areas, data are distributed to different clients, entities,and institutions. To collect more data to improve the performance, companies will also collectand analyze data from individuals, which comes with issues of user privacy and data security. Forexample, in medical applications, a hospital or medical institution is forbidden to share medicaldata according to regulations (e.g., HIPAA). Another example is that smart wearable devices arealways collecting sensitive individual data, which are critical for wearable applications. However,sharing these data for model training also raises concerns about privacy leakage.

In a nutshell, sharing data and distributed computation is a trend in the era of big data,as it can (1) improve the computational efficiency, and (2) improve the model performance. Inthe meanwhile, the increasing awareness of privacy and data security requires a DML systemto take privacy-preserving into consideration. Therefore, building a privacy-motivated DMLsystem has become an important research direction. In this section, we start from a privacy-preserving decision tree example and further introduce several privacy-preserving techniquesand their applications in a DML system.

For a privacy-preserving DML system, it generally protects some or all of the followinginformation [Vepakomma et al., 2018].

1. Input training data;

2. Output predicted labels;

3. Model information, including parameters, architecture, and loss function; and

4. Identifiable information, such as which site a record comes from.

# 3.3.1 PRIVACY-PRESERVING DECISION TREES

The decision tree is an important kind of supervised ML algorithm, which is widely used in clas-sification and regression. The learned model of a decision tree is explainable and understandable

to people. There are variants of decision trees, and ID3 [Quinlan, 1986] is one of the most fa-mous of them. In distributed decision tree algorithms, it is normally divided into two categoriesaccording to the data distribution, formally defined as follows.

1. Horizontally partitioned datasets:

$$
\mathcal {X} _ {i} = \mathcal {X} _ {j}, \mathcal {I} _ {i} \neq \mathcal {I} _ {j} \forall \mathcal {D} _ {i} \neq \mathcal {D} _ {j}.
$$

2. Vertically partitioned datasets:

$$
\mathcal {X} _ {i} \neq \mathcal {X} _ {j}, \mathcal {I} _ {i} = \mathcal {I} _ {j} \forall \mathcal {D} _ {i} \neq \mathcal {D} _ {j},
$$

where $\mathcal { X }$ is the feature space of the data, and $\mathcal { T }$ is the sample space (i.e., the identification ofeach sample) of the data. We next provide an explanation on this definition.

In the scenario of the horizontally partitioned dataset, each participant (noted as an en-tity) in the DML system owns different samples, and samples in all entities have the sameattribute categories. For example, the data collected by different wearable devices have the sameset of attributes since the sensors of the devices are the same. However, as a result of differentenvironments, the data samples collected by different entities should be different.

In the scenario of the vertically partitioned dataset, the attribute sets of data owned bydifferent entities are different, but these samples are possibly referring to the same group ofusers. For example, the medical records of the same patient in different medical institutionsrecord different physiological indices or disease examination results.

For horizontally partitioned DML, the aggregation of samples is equivalent to enlargingthe dataset, while in the vertically partitioned scenario, it is similar to augmenting the featuresof the samples. In either way, distributed training provides a manner to expand the dataset.

Different from other ML algorithms, the data partition is critical for decision trees, be-cause the learning of a decision tree needs to determine the split of the attribute set, dependingon both the attribute category and the number of samples under a particular attribute with aclass label.

Lindell and Pinkas [2002] first propose a privacy-preserving distributed decision tree al-gorithm based on the horizontally partitioned dataset. They introduced an oblivious secure pro-tocol which computes $( v _ { 1 } + v _ { 2 } ) \log ( v _ { 1 } + v _ { 2 } )$ without revealing each value to other participants.This secure computation allows the distributed decision tree to privately calculate the node splitacross the samples in different participants. Wang et al. [2006] and Du and Zhan [2002] firstaddressed the problem of designing a vertically partitioned distributed decision tree with privacyprotection. However, their solutions assume all of the participants own the class attribute.

Fang and Yang [2008] completed their work by allowing only one entity in the verticallypartitioned distributed system to have the class attribute. Their work is based on ID3-tree, wherethe learning of the tree is decomposed into different components including attribute checking,distribution counts, class checking, attribute information gain checking, and information gain

# 42 3. DISTRIBUTED MACHINE LEARNING

computation. Each part of distributed computation is protected by secure protocols. Besides,this work provides a loosely secure version and a completely secure version, providing a trade-offbetween efficiency and security.

Cheng et al. [2019] proposed a vertically distributed boosting tree based on secure setintersection protocol and partially homomorphic encryption. They prove that their method is notonly secure and privacy-preserving but also lossless. There are also privacy-preserving distributeddecision trees using differential privacy (DP) to protect individual privacy by adding noise to thestatistics [Jagannathan et al., 2009].

The development of privacy-motivated decision tree algorithms considers the data parti-tion and utility of privacy-preserving tools. As a preliminary of privacy-preserving distributedML systems, we briefly introduce some commonly used tools for privacy and security protectionsin the next subsection.

# 3.3.2 PRIVACY-PRESERVING TECHNIQUES

In privacy-motivated DML system, the popular tools to protect data privacy can be roughlycategorized into the following two categories.

1. Obfuscation: to randomize or modify the data to conceal a certain level of privacy, e.g.,DP.

2. Cryptographic Methods: to secure the distributed computation process without revealinginput values to other participants, e.g., secure multi-party computation (MPC), includ-ing oblivious transfer (OT), secret sharing (SS), garbled circuit (GC), and homomorphicencryption (HE).

Please refer to Section 2.4 for a quick review of the aforementioned privacy-preserving tech-niques.

# 3.3.3 PRIVACY-PRESERVING DML SCHEMES

In the following, we give a quick review of representative works on privacy-preserving DML,emphasizing on how they utilize privacy protection tools mentioned above to protect the dataand model security in a distributed environment. According to the aforementioned tools, wefirst summarize the DML algorithms using obfuscation and then introduce those algorithmsthat use cryptographic methods.

Chaudhuri and Monteleoni [2009] proposed a privacy-preserving logistic regression al-gorithm based on DP. They tackle the optimization over randomized data, making it possible totake a balance between model performance and privacy protection and make the privacy boundtighter. Following the definition given by Dwork [2008], they prove that their work guarantees$\varepsilon$ -differential privacy, and provide a novel algorithm with better performance. In the proposedwork, a randomized vector is generated using a Gamma function, which participates in the

optimization of the logistic regression parameter . Moreover, they concluded that their workreveals the relation between perturbation-based privacy protection and regularization.

Wild and Mangasarian [2007] and Mangasarian et al. [2008] studied privacy-preservingsupport vector machines (PPSVMs) on horizontally and vertically partitioned datasets, respec-tively. They concealed the originally learned kernel with a randomly generated kernel, achievingcomparable performance to the non-private SVMs. The privacy proof is based on the fact thatthere are infinite possible input data that can be recovered from the perturbed kernel. Therefore,sharing the perturbed kernel will not cause privacy leakage. However, these methods requireparticipants to share the randomly generated kernel, limiting the application of these methods.

Apart from logistic regression, SVMs, and decision trees, perturbation-based privacy pro-tection methods are also widely used in DL systems. With reference to the survey [Zhang et al.,2018], we selectively introduce some representative works. Song et al. [2013] proposed a differ-entially private stochastic gradient descent algorithm (DP-SGD), which clips the gradients andinjects noise to them during training, so that the learned DL model preserves $( \varepsilon , \delta )$ -differentialprivacy. Different from previous works, Song et al. [2013] and Shokri and Shmatikov [2015]utilize another obfuscation method, i.e., a distributed selective stochastic gradient descent algo-rithm. It allows the local model to selectively share part of the parameters, avoiding informationleakage and also preserving the performance of the joint learning model. Except for jointly learn-ing a prediction model, Dwork [2011] proposed a differentially private autoencoder to learn therepresentation of local data.

DP is also used for unsupervised learning. Park et al. [2016] proposed a differentiallyprivate EM algorithm (DP-EM) based on moment perturbation. They utilize moment accoun-tants [Abadi et al., 2016] and zCDP to reduce the magnitude of noise added to the EM processwhile maintaining the same level of privacy protection compared to the original analysis tech-nique. In their work, they compare different randomization mechanisms and their compositionsettings, and find that in DP-EM, using Gaussian mechanism in every stage of EM can achievethe tightest privacy budget.

In conclusion, owing to the computational efficiency and implementation convenience,obfuscation-based privacy-preserving techniques are popular in privacy-motivated DML sys-tems. Meanwhile, perturbation affects the utility of the data and model. In practice, researchershave to make a tradeoff between privacy protection and performance. Compared to obfuscation-based methods, cryptographic methods do not need to sacrifice data accuracy and model per-formance.

In Aono et al. [2016], authors utilize HE to protect the data during the training of logisticregression. Their method uses a two-degree approximation to the log-linear objective function,making the training process compatible with the additive HE method, which improves compu-tational efficiency while maintaining a comparable performance. Besides, they claim that theiroutput is compatible with DP. They also analyze the storage and computation complexity oftheir system, showing that their system supports large-scale distributed computation. Fienberg

et al. [2006] also considered linear regression (LR) on the horizontally partitioned dataset, uti-lizing MPC method to aggregate the calculation. However, in their setting, the features arecategorical, which means the computation space is small. Slavkovic et al. [2007] made signifi-cant progress, using secure summation protocol and secure matrix multiplication for the aggregationof distributed learning of LR, which supports both vertical and horizontal data partition.

Vaidya and Clifton [2004] designed a secure parameter sharing mechanism for privacy-preserving naive Bayes classifiers on vertically partitioned data, where each participant con-tributes to a conditionally independent probability. Each individual parameter is indistinguish-able from random noise, while only the aggregation is meaningful. However, the extra com-putational complexity for secure computation is also significant. Yu et al. [2006] and Zhan andMatwin [2007] introduce secure dot product and secure summation protocol to protect the data dur-ing kernel computation in SVMs. Xu et al. [2015] embed the secure summation protocol into theReducer of Hadoop system, implementing an efficient distributed SVM system that supportslarge-scale data. Similarly, Lin et al. [2005] use secure summation protocol to aggregate the localcomputation results for distributed EM algorithm, preventing data leakage from local compu-tation results.

As for DL, one of the most representative work is SecureAggregation, proposed byBonawitz et al. [2016]. This work is based on the federated learning algorithm, FedAvg, firstadopted for federated learning by Google [McMahan et al., 2016b], further introducing secretsharing, and oblivious transfer to FedAvg, in a complex mobile environment where the commu-nication is expensive, and the dropout and join-in of clients are frequent. To ensure data security,each leaving data is randomized, and only the aggregation of these shares is meaningful. To re-duce the communication cost, they only exchange random seed using secure key-exchange protocolinstead of random noise. To handle the challenge that clients can dropout unexpectedly, theyuse secret sharing so even some client are lost, the system can still recover the data using theremaining shares. Besides SecureAggregation, there are other DL algorithms that use MPCmethods [Liu et al., 2016, Shokri and Shmatikov, 2015].

In addition, Mohassel and Zhang [2017] propose a set of privacy-preserving ML al-gorithm based on MPC methods, supporting LR, logistic regression, and SGD, and provide$\mathrm { C } { + } { + }$ implementation. Different from obfuscation-based privacy-preserving DML algorithms,cryptographic method-based methods emphasize on taking balance between computational andcommunication complexity, and security.

In the above, we have briefly introduced some representative privacy-motivated DMLalgorithms, as well as some widely used privacy-protection tools. For a more detailed treatmentof this topic, the following surveys Vepakomma et al. [2018], Zhang et al. [2018] and Mendesand Vilela [2017] are recommended.

# 3.4 PRIVACY-PRESERVING GRADIENT DESCENT

Gradient descent method is one of the central algorithms in ML. Privacy-preserving gradi-ent descent methods have been widely studied. In this section, we review different privacy-preserving techniques proposed for gradient descent. There is a trade-off between efficiency,accuracy and privacy protection. Developing good privacy-preserving gradient descent methodsneeds an artful balance of the efficiency-accuracy-privacy trade-off.

Methods preferring higher efficiency while facing less privacy concern may sacrifice dataprivacy for higher computational efficiency. For example, the gradients are sent to a coordinatorin plain-text for model update in the gradient averaging approach [McMahan et al., 2016b], totrade privacy for efficiency without degrading the global learning accuracy. Methods aiming forthe highest data privacy and security generally choose to use HE and MPC, which in turn leadsto high computation complexity and communication overhead.

In addition to the approaches discussed in Chapter 2, there also exist some other privacy-preserving approaches with different privacy guarantees. In some cases, the privacy model onlyaims to guarantee that the raw form of input data of each party could not be revealed by theadversary. By providing such weak privacy guarantees, researchers aim to trade privacy for effi-ciency. Proposed approaches vary significantly.

Typical privacy-preserving gradient descent approaches include naive federated learning,algebraic approaches, sparse gradient update approaches, obfuscation approaches and crypto-graphic approaches (e.g., HE and MPC). Obfuscation approaches are based on randomiza-tion, generalization or suppression mechanisms (e.g., gradient quantization, DP, k-anonymity).Generally in the naive federated learning, algebraic approaches and sparse gradient update ap-proaches, each party sends clear-text gradient to the coordinator for model update, which onlyprotects raw data and yields weak privacy guarantee with quite high efficiency. The sparse gra-dient update approaches also trade accuracy for efficiency and privacy by updating a subset ofentries in the gradient. Approaches based on randomization mechanism such as DP and Gaus-sian Random Projection (GRP) trade accuracy for privacy by adding random noise to the dataor gradient. Approaches based on the generalization and suppression also trade accuracy for pri-vacy by generalizing attributes or removing some instances. We review here some approachesfor privacy-preserving gradient descent with roughly increasing privacy guarantees.

# 3.4.1 VANILLA FEDERATED LEARNING

Federated Averaging (FedAvg) was first employed for federated learning over horizontally parti-tioned dataset. In federated averaging, each party uploads clear-text gradient to a coordinator (ora trusted dealer, or a parameter server) independently, then the coordinator computes the aver-age of the gradients and update the model. Finally, the coordinator sends the clear-text updatedmodel back to each party [McMahan et al., 2016b]. When the dataset is vertically partitioned,the model is distributed among the parties. In gradient descent methods, the objective functioncan be decomposed into a differentiable function and a linearly separable function [Wan, 2007].

To conduct gradient descent, each party applies its data on its partial model to get intermediatecomputation results and send them to the coordinator in clear-text. The coordinator accumu-lates the intermediate results and evaluates the differentiable function to compute the loss andgradient. Finally, the coordinator updates the whole and send the updated partial model to eachcorresponding party. It is assumed that the coordinator is honest and incurious, and does notcollude with any party. If the coordinator is corrupted, the gradient information of each partycan be disclosed. Although the raw form of training data is not likely to be inferred from the gra-dient of each party, it has been demonstrated that it is possible to infer considerable informationfrom the gradient uploaded from each party [Aono et al., 2018].

# 3.4.2 PRIVACY-PRESERVING METHODS

# Algebraic Approaches

Algebraic approaches aim to protect raw training data by leveraging the algebraic propertiesof data transmitted. They preserve privacy by guaranteeing that there exist infinite valid input-output pairs of each honest party against the input and output of the adversaries, that is, the rawform of input data is protected. Wan [2007] proposed a secure gradient descent approach fortwo-party vertical federated learning by decomposing the target function into a differentiablefunction and a linearly separable function. In this approach, the model parameters of the twoparties are mutually masked, and only the clear-text gradient is disclosed and used for modelupdate. Such approaches implicitly radically assumes that each party has no knowledge of therecords of the other party. If a small subset of records are disclosed to the other party (e.g., bydata poisoning), the model can be easily disclosed via solving-equation attack.

To defend against the equation-solving attack, a secure two-party computation approachfor vertical federated linear regression and classification is proposed by introducing the concept ofk-secure [Du et al., 2004]. In this approach, the instances are aligned and the dependent attributeis in public. Arithmetic secret sharing is used here. As the addition operation in arithmetic secretsharing is done locally, thus it is information-theoretical secure. The two-party multiplicationis conducted as follows. First, the two parties jointly generate a random invertible matrix M.Then, one party A does matrix multiplication with its input matrix A to the left-side and right-side sub-matrix of M in turn, and sends the first ${ \bf A } _ { 1 }$ result to party B. The other party B doesmatrix multiplication with its input matrix to the top-side and bottom-side sub-matrix of M inturn, and send the second result $\mathbf { B _ { 2 } }$ to party A. Finally, both parties compute $\mathbf { V } _ { a } = \mathbf { A } _ { 1 } \cdot \mathbf { B _ { 1 } }$ and$\mathbf { V } _ { b } = \mathbf { A } _ { 2 } \cdot \mathbf { B _ { 2 } }$ , where $\mathbf { V } _ { a } + \mathbf { V } _ { b } = \mathbf { A } \cdot \mathbf { B }$ .

The security of this protocol is based on the algebraic property that $2 n ^ { 2 }$ equations can-not determine $n \times N$ variables, where $N > > n$ . Although the gradient descent approach is notdemonstrated in this study, it is straightforward to implement it according to what is discussedin Chapter 2.

# Sparse Gradient Update Approaches

The sparse gradient update approaches preserve privacy by updating only a subset of gradients.Such approaches trade accuracy for efficiency and weak privacy. As the gradient is in the clear,they also trade privacy for efficiency. For example, Shokri and Shmatikov [2015] disclose onlya subset of clear-text gradient parameters to the coordinator for model update. Strategies forimproving communication efficiency include structured update and sketched update [Konecnýet al., 2016a]. The structured update strategy only updates a sparse or a low-rank gradient matrix,and the sketched update strategy utilizes subsampling and quantization to eliminate the volumeof gradients.

Multi-objective evolutionary computation is also explored in federated learning to learnsparse model parameters [Zhu and Jin, 2018]. Sparse gradient update and gradient compressionare widely studied for stronger privacy preservation. However, there is little formal analysis ofthe privacy preserved by the gradient compression.

# Obfuscation Approaches

Obfuscation approaches obfuscate data via randomization, generalization and suppression,which leads to an improvement of privacy at the cost of a deterioration of accuracy. In fed-erated learning, local differential privacy (LDP) can be used by applying an additive noise maskto the gradient of each party. Jiang et al. [2019] propose an approach that applies independentGaussian random projection (GRP) to protect the raw form of training data. Each participantfirst generates a Gaussian random matrix and project its raw training data for obfuscation. Thenthe obfuscated data are sent to the coordinator for model training. The privacy protected is onlythe raw form of the training data of each participant. The GRP used here also faces a problemof scalability in terms of both number of participants and attribute dimension. The gradientquantization strategy quantizes each gradient value to an adjacent value, which trades modelaccuracy for efficiency and privacy [Konecný et al., 2016a].

# Cryptographic Approaches

The approaches discussed above disclose clear-text gradient of each party to the coordinator oreach other parties. In contrast, cryptographic approaches leverage HE and MPC to preserve theprivacy of the gradient of each party in the gradient descent procedure. The security models varyfrom security against honest-but-curious adversaries to security against malicious adversaries,and the corruption assumptions also vary a lot. In addition to the security model, the informationdisclosed by each approach also varies. Cryptographic approaches trade efficiency for privacy.As it could be very computation or communication inefficient, the approximations of nonlinearfunctions are generally introduced to further trade accuracy for efficiency.

The secure aggregation approaches introduce a coordinator that is only allowed to learn theclear-text average of a group of gradients. Secure aggregation preserves the privacy of each party’sgradient via Shamir’s threshold secret sharing scheme, so that the coordinator can only disclose

the average of a group of gradients [Bonawitz et al., 2016]. However, when the coordinatorand $n - 1$ parties collude in a group with $n$ parties, the input gradient can be easily disclosed.As such secure aggregation is anonymous, extreme poisoning attack may occur. Bonawitz et al.[2016] proposes “trimmed mean,” where the gradients are trimmed coordinate-wisely to preventextreme poisoning adversary.

Other cryptographic approaches introduce one or more non-colluding coordinators, whilethe coordinators are not allowed to learn anything about the gradient and the model. For HE-based approaches, this can be done by adding a random mask to the value to be decrypted [Liu etal., 2019]. For MPC-based approaches, the trusted dealer can be asked to generate computation-independent materials (e.g., Beaver triples) [Beaver, 1991]. When there are multiple non-colluding coordinators introduced, each party generates secret sharing of its private data andshares it with each coordinator accordingly [Mohassel and Zhang, 2017, Wagh et al., 2018].The gradient descent is then conducted between the coordinators.

When it is infeasible to introduce a coordinator, some coordinator-free cryptographic ap-proaches can be adopted, where the secure multi-party gradient descent is conducted so that eachparty can learn nothing beyond its output and its input. Existing MPC protocols secure againsta majority of colluding malicious adversaries include SPDZ [Damård et al., 2011], $\mathrm { S P D } Z _ { 2 \mathrm { k } }$ ,Overdrive [Keller et al., 2018], and MASCOT [Keller et al., 2016]. In such approaches, anoffline phase is implemented where the Beaver triples are generated by MPC before securemulti-party gradient descent. Bonawitz et al. [2016] demonstrate an actively-secure MPC pro-tocol based on $\mathrm { S P D } Z _ { 2 \mathrm { k } }$ for decision tree and SVM. The gradient descent functions can also beevaluated similarly based on the $\mathrm { S P D } Z _ { 2 \mathrm { k } }$ protocol.

# 3.5 SUMMARY

This chapter presents a brief introduction of the scalability-motivated DML and the privacy-motivated DML. The scalability-motivated DML is widely employed for addressing the com-putation resource and memory limitations in large-scale ML problems. Parallelism techniques(such as data parallelism, model parallelism, and hybrid parallelism) are the major choices forimplementing and expanding the scalability-motivated DML systems. The privacy-motivatedDML is primarily adopted for preserving user privacy and ensuring data security with decen-tralized data sources. MPC, HE and DP are the main privacy-preserving techniques for realiz-ing the privacy-motivated DML. Privacy-preserving gradient descent methods have also beenwidely used for empowering the privacy-motivated DML.

DML has received abundant attention in past years, and has been fast-developed intoopen-source and commercial products. Yet, there are still practical challenges that the existingDML systems cannot address. Federated learning is a special type of DML, and it can furtheraddress the issues that the conventional DML systems are faced with and enable us to buildprivacy-preserving AI. We will elaborate with details in the subsequent chapters on federatedlearning.

# Horizontal Federated Learning

In this chapter, we introduce horizontal federated learning (HFL), covering the concept, archi-tecture, application examples, and related works, as well as open research challenges.

# 4.1 THE DEFINITION OF HFL

HFL, a.k.a. sample-partitioned federated learning, or example-partitioned federated learn-ing [Kairouz et al., 2019], can be applied in scenarios in which datasets at different sites shareoverlapping feature space but differ in sample space, as illustrated in Figure 4.1. It resembles thesituation that data is horizontally partitioned inside a tabular view. In fact, the word “horizontal”comes from the term “horizontal partition,” which is widely used in the context of the tradi-tional tabular view of a database (e.g., rows of a table are horizontally partitioned into differentgroups and each row contains complete data features). For example, two regional banks mayhave very different user groups from their respective regions, and the intersection set of theirusers is very small. However, their business models are very similar. Hence, the feature spacesof their datasets are the same. Formally, we summarize the conditions for HFL as:

$$
\mathcal {X} _ {i} = \mathcal {X} _ {j}, \mathcal {Y} _ {i} = \mathcal {Y} _ {j}, I _ {i} \neq I _ {j}, \forall \mathcal {D} _ {i}, \mathcal {D} _ {j}, i \neq j, \tag {4.1}
$$

where the data feature space and label space pair of the two parties, i.e., $( { \mathcal { X } } _ { i } , { \mathcal { N } } _ { i } )$ and $( \mathscr { X } _ { j } , \mathscr { y } _ { j } )$ ,are assumed to be the same, whereas the user identifiers $I _ { i }$ and $I _ { j }$ are assumed to be different;$\mathcal { D } _ { i }$ and $\mathcal { D } _ { j }$ denote the datasets of the ith party and the $j$ th party, respectively.

Security of an HFL system. An HFL system typically assumes honest participants andsecurity against an honest-but-curious server [Phong et al., 2018, Bonawitz et al., 2017]. Thatis, only the server can compromise the user privacy and data security of the participants.

Shokri and Shmatikov [2015] proposed a collaborative deep learning (DL) scheme whereparticipants train models independently and share only subsets of model parameter updates,which is a special form of HFL. In 2016, researchers at Google proposed an HFL-based solutionfor Android smartphone model updates [McMahan et al., 2016a]. In this framework, a singleAndroid smartphone updates the model parameters locally and uploads the model parametersto the Android cloud, thus jointly training the federated model together with other Androidsmartphones.

A secure aggregation scheme for protecting the privacy of the user model updates un-der this federated learning framework was introduced in Bonawitz et al. [2017]. More recently,

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/c830b4ff720fad41eeb53d850f30ae2d001fefe7c552504d2be3854ea1a450ab.jpg)



Figure 4.1: Illustration of HFL, a.k.a. sample-partitioned federated learning [Yang et al., 2019].


Phong et al. [2018] applied additively homomorphic encryption for model parameter aggrega-tion to provide security against an untrustworthy central server.

In Smith et al. [2017], a multi-task style federated learning system is proposed to allowmultiple sites to complete different tasks, while sharing knowledge and preserving security. Theirproposed multi-task learning model can also address the issues of high communication costs,stragglers, and fault tolerance.

In McMahan et al. [2016a], the authors proposed a secure client-server structure wherethe federated learning system partitions data by users, and allows models built at client devicesto collaborate at the server site to build a global federated model. The process of model buildingensures that there is no data leakage. Likewise, in Konecný et al. [2016b], the authors proposedmethods to reduce the communication cost to facilitate the training of federated models based ondata distributed over mobile clients. More recently, a compression approach called Deep Gradi-ent Compression [Lin et al., 2018] is proposed to greatly reduce the communication bandwidthin large-scale distributed model training.

Security proof has been provided in these works. Recently, another security model consid-ering malicious user [Hitaj et al., 2017] is also proposed, posing additional privacy challenges.At the end of federated training, the aggregated model and the entire model parameters areexposed to all participants.

# 4.2 ARCHITECTURE OF HFL

In this section, we describe two popular architectures for HFL systems, namely the client-serverarchitecture and the peer-to-peer architecture.

# 4.2.1 THE CLIENT-SERVER ARCHITECTURE

A typical client-server architecture of an HFL system is shown in Figure 4.2, which is alsoknown as master-worker architecture. In this system, $K$ participants (also known as clients orusers or parties) with the same data structure collaboratively train a machine learning (ML)model with the help of a server (also known as parameter server or aggregation server or coor-dinator). A typical assumption is that the participants are honest whereas the server is honest-but-curious. Therefore, the aim is to prevent leakage of information from any participants to theserver [Phong et al., 2018]. The training process of such an HFL system usually consists of thefollowing four steps.

• Step 1: Participants locally compute training gradients, mask a selection of gradients withencryption [Phong et al., 2018], differential privacy [Abadi et al., 2016], or secret shar-ing [Bonawitz et al., 2017] techniques, and send the masked results to the server.

• Step 2: The server performs secure aggregation, e.g., via taking weighted average.

• Step 3: The server sends back the aggregated results to the participants.

• Step 4: The participants update their respective models with the decrypted gradients.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/fee73e60747873ed2112b576a3d620bfb4ee9c9d71cb210a1a4e7770d12061f5.jpg)



Figure 4.2: Exemplary client-server architecture for an HFL system [Yang et al., 2019].


Iterations through the above steps continue until the loss function converges or until themaximum number of allowable iterations is reached or until the maximum allowable trainingtime is reached. This architecture is independent of specific ML algorithms (e.g., logistic regres-sion and DNN, and all participants will share the same final model parameters.

Note that in the above steps, it is described that the participants send gradients to theserver, which in turn, aggregates the received gradients. We call this approach gradient averag-ing [Tang et al., 2019, Su and Chen, 2018]. Gradient averaging is also known as synchronousstochastic gradient descent (SGD) or federated SGD (FedSGD) [McMahan et al., 2016a, Chen

et al., 2017]. Alternatively, instead of gradients, the participants can share model weights. Thatis, participants locally compute model weights and send them to the server [Phong and Phuong,2019]. The server aggregates the received local model weights and sends the aggregated resultsback to the participants. We call this approach model averaging [McMahan et al., 2016a, Yu etal., 2018, Xu et al., 2018]. In the extreme case, in which model parameters are averaged aftereach weight update carried out locally at the participants and the participants all start with thesame initial model weights, model averaging is equivalent to gradient averaging [Su and Chen,2018, McMahan et al., 2016a]. We summarize the comparison between gradient averaging andmodel averaging in Table 4.1. Note that both gradient averaging and model averaging are re-ferred to as federated averaging (FedAvg) in McMahan et al. [2016a].


Table 4.1: Comparison between gradient averaging and model averaging [Tang et al., 2019, Suand Chen, 2018]


<table><tr><td>Method</td><td>Advantage</td><td>Disadvantage</td></tr><tr><td>Gradient averaging</td><td>Accurate gradient informationGuaranteed convergence</td><td>Heavy communicationRequire reliable connection</td></tr><tr><td>Model averaging</td><td>Not bound to SGDTolerance of update lossInfrequent synchronization</td><td>No guarantee of convergencePerformance loss</td></tr></table>

The above architecture is able to prevent data leakage against a semi-honest server, ifgradient aggregation is performed with secure multi-party computation [Bonawitz et al., 2017]or additively homomorphic encryption [Phong et al., 2018]. However, it may be vulnerableto attacks by a malicious participant training a Generative Adversarial Network (GAN) in thecollaborative learning process [Hitaj et al., 2017].

The client-server architecture appears similar to the architecture of a distributed machinelearning (DML) system, especially the data-parallel paradigm (see also Section 3.2) of DML.HFL also resembles geo-distributed machine learning (GDML) [Xu et al., 2018, Cano et al.,2016, Hsieh et al., 2017]. A parameter server [Li et al., 2014, Ho et al., 2013] is a typicalelement in DML. As a tool to accelerate the training process, the parameter server stores data ondistributed working nodes, allocates data and computing resources through a central schedulingnode, so as to train the model more efficiently. For HFL, a data owner is a working party. It hasfull autonomy to operate on its local data, and can decide when and how to join and contributeto an HFL system. In the parameter server paradigm [Li et al., 2014, Ho et al., 2013], thecentral node always takes control, while an HFL system is faced with a more complex learningenvironment. Further, HFL takes into account data privacy protection during model training.Effective measures to protect data privacy can better cope with the increasingly stringent userprivacy and data security requirements coming up in the near future. Finally, in an HFL system,

the data held of the different participants are not identically distributed in most of the practicalapplications, while in a DML system, the data held by the different computing nodes normallyfollow the same distribution.

# 4.2.2 THE PEER-TO-PEER ARCHITECTURE

In addition to the client-server architecture discussed above, an HFL system can also make use ofthe peer-to-peer architecture shown in Figure 4.3 [Zantedeschi et al., 2019, Chang et al., 2017,2018, Phong and Phuong, 2019]. Under the peer-to-peer architecture, there is no central serveror coordinator. In such scenarios, the $K$ participants of an HFL system are also called trainersor distributed trainers or workers. Each trainer is responsible for training the same ML or DLmodel (e.g., a DNN model) using only its local data. Further, the trainers need secure channelsto transfer the model weights to each other. To ensure secure communications between any twotrainers, security measures, such as public key based encryption schemes, can be adopted.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/bfe805d8e630ff2382da7b2734f4c0083eb1254de20bb27c7c030af928cc251f.jpg)



Figure 4.3: Exemplary peer-to-peer architecture for an HFL system.


Since there is no central server, the trainers must agree to the order of sending and receiv-ing model weights in advance. There are mainly two ways to do this.

• Cyclic transfer. In the cyclic transfer mode, the trainers are organized into a chain. Thefirst trainer (i.e., the top of the chain) sends its current model weights to its downstreamtrainer. One trainer receives model weights from its upstream trainer, and it updates thereceived model weights using mini-batches of training data from its own dataset. Then, itsends the updated model weights to its downstream trainer. For example, from trainer 1

to trainer 2, from trainer 2 to trainer 3; : : :, from trainer $( K - 1 )$ to trainer $K$ , and fromtrainer $K$ back to trainer 1. This procedure is repeated until the model weights convergeor until the maximum number of iterations is reached or until the maximum allowabletraining time is reached.

• Random transfer. The $k$ th trainer selects a number $i$ from $\{ 1 , \ldots , L \} \setminus \{ k \}$ at random withequal probability, and sends its model weights to trainer i. When the ith trainer receivesmodel weights from the kth trainer, it updates the received model weights using mini-batches of training data from its own dataset. Then, the ith trainer also selects a number$j$ in $\{ 1 , \ldots , L \} \setminus \{ i \}$ at random and with equal probability, and sends its model weights totrainer $j$ . This procedure takes place concurrently among the $K$ trainers until the trainersagree that the model weights have converged or until the maximum allowable training timeis reached. This method is also known as Gossip Learning [Hardy et al., 2018, Hegedüset al., 2019].

Sharing model weights is used as an example in the above descriptions. It is also possiblefor the trainers to share gradients, such as using a gossip SGD-based approach, see, e.g., Liu etal. [2018] and Daily et al. [2018], for more details.

Compared with the client-server architecture, the obvious advantage of the peer-to-peerarchitecture is the possibility to remove the central server (also known as server, parameter server,aggregation server, or coordinator), which may not be available in practical applications, and itclears the chance of leaking information to the server. However, there are several disadvantages.For instance, in the cyclic transfer mode, since there is no central server, weight parameters areupdated serially rather than in parallel batches, which takes more time to train a model.

# 4.2.3 GLOBAL MODEL EVALUATION

In HFL, model training and evaluation are carried out distributively at each participant, and it isimpossible to access the datasets of the participants. As a consequence, each participant can easilytest the mode performance using its local testing dataset to get the local model performance,but it takes more efforts to get the global model performance across all participants. Here, localmodel performance means the performance of an HFL model examined on the local test datasetof a single participant, and global model performance refers to the performance of an HFLmodel evaluated on the test datasets of all the participants. Model performance may be expressedin terms of accuracy, precision, recall, and area under the receiver operating characteristic curve(AUC), etc. For ease of elaboration, we use a two-class classification task as an example to explainhow we can obtain the global model performance in HFL.

For the client-server architecture, the participants and the coordinator can cooperate to getthe global model performance. During model training process and after model training beingcompleted in HFL, we can obtain the global model performance according to the followingsteps.

• Step 1: The kth participant evaluates the performance of the current HFL model using itslocal test dataset. For the two-class classification task, this step generates the local modelevaluation results such as $\left( N _ { T P } ^ { k } , N _ { F P } ^ { k } , N _ { T N } ^ { k } , N _ { F N } ^ { k } \right)$ , where $N _ { T P } ^ { k }$ , $\bar { N } _ { F P } ^ { k }$ , $N _ { T N } ^ { k }$ , and $N _ { F N } ^ { k }$ denotethe number of true positive results, the number of false positive results, the number of truenegative results, and the number of false negative results, respectively, for $k = 1 , 2 , \ldots , K$ .

• Step 2: The $k$ th participant sends the local model evaluation results $\left( N _ { T P } ^ { k } , N _ { F P } ^ { k } , N _ { T N } ^ { k } , N _ { F N } ^ { k } \right)$to the coordinator, for $k = 1 , 2 , \dots , K$ .

• Step 3: After collecting the local model evaluation results of the $K$ participants, i.e.,$\{ ( \bar { N _ { T P } ^ { k } } , N _ { F P } ^ { k } , N _ { T N } ^ { k } , N _ { F N } ^ { k } ) \} _ { k = 1 } ^ { \bar { K } }$ , the coordinator can calculate the global model performance.For example, for the two-class classification task, the global model recall can be computedas: $\frac { \sum _ { k = 1 } ^ { \hat { K } } N _ { T P } ^ { k } } { \sum _ { k = 1 } ^ { K } \left( N _ { T P } ^ { k } + N _ { F N } ^ { k } \right) }$ .

• Step 4: The coordinator then sends the computed global model performance (e.g., accu-racy, precision, recall, and AUC, etc.) back to all the participants.

For the peer-to-peer architecture, since there is no central coordinator, it would be morecomplicated to obtain global model performance. One possible way is to pick one of the trainersto serve as a temporary coordinator. Then, we can follow the above procedure proposed for theclient-server architecture to obtain the global model performance for the peer-to-peer archi-tecture. This method is recommended for evaluating the final HFL model after the training iscompleted. However, if we apply this method during the training process, it would overburdenthe temporary coordinator, which may not be acceptable if the trainers are mobile or IoT deviceswith limited resources (e.g., battery). One possible way to remedy this issue is to ask the trainersto take turns to act as the temporary coordinator.

# 4.3 THE FEDERATED AVERAGING ALGORITHM

In McMahan et al. [2016a,b], the federated averaging (FedAvg) algorithm was employed forfederated model training in HFL systems. We review the FedAvg algorithm and its securedversion in this section, assuming a client-server architecture. Note that the FedAvg algorithm isalso known as parallel restarted SGD and local SGD [Yu et al., 2018, Haddadpour et al., 2019],as opposed to parallel mini-batch SGD.

# 4.3.1 FEDERATED OPTIMIZATION

The optimization problem arising from federated learning is referred to as federated optimiza-tion [Li et al., 2019, McMahan et al., 2016b], so to name it differently from distributed opti-mization. In fact, federated optimization has several key properties that differentiate it from aconventional distributed optimization problem [McMahan et al., 2016b, Xu et al., 2018, Canoet al., 2016].

• Non-independent identical distributions (Non-IID) of datasets. For distributed opti-mization within a data center, it is possible to ensure that different computing nodes haveIID datasets so that all local updates look very similar. In federated optimization, this can-not be guaranteed. The data owned by different participants may follow completely differ-ent distributions, i.e., we cannot make IID assumptions about the decentralized datasetsin federated learning [Li et al., 2019, Liu et al., 2018, Sattler et al., 2019]. For exam-ple, while similar participants might have similar local training data, two randomly pickedparticipants might produce very different model weight updates or gradient updates.

• Unbalanced number of data points. For distributed optimization within a data center, it ispossible to divide the data equally among the computing nodes. However, in realistic sce-narios, different participants usually have very different volumes of training datasets [Chenet al., 2019, Li et al., 2018, Duan, 2019]. For example, some participants may hold only ahandful of data points, while others might have large amounts of data.

• Huge number of participants. For distributed optimization within a data center, thenumber of parallel computing nodes can easily be controlled. However, since ML or DLgenerally requires a lot of data, the applications that use federated learning may need toinvolve many participants, especially with mobile devices [Bonawitz and Eichner et al.,2019]. Every one of these participants can theoretically participate in federated learning,making it far more distributed than that within a data center.

• Slow and unreliable communication links. In a data center, it is expected that nodes cancommunicate quickly with each other and that packets are almost never lost. However,in federated learning, communication between clients and the server relies on existingInternet connections. For example, uploads (from client to server) are typically going tobe much slower than downloads, especially if the connection is from a mobile terminal.Some clients might also temporally lose connections to the Internet [Tang et al., 2019,Hartmann, 2019].

To address the above challenges faced in federated optimization, McMahan et al. firstadopted the FedAvg algorithm for federated optimization [McMahan et al., 2016b]. The focusof FedAvg [McMahan et al., 2016a,b] is on non-convex objective functions commonly seenwhen training DNNs. FedAvg is applicable to any finite-sum objective function of the followingform:

$$
\min  _ {w \in R ^ {d}} f (w) = \frac {1}{n} \sum_ {i = 1} ^ {n} f _ {i} (w), \tag {4.2}
$$

where n denotes the number of data points and $w \in R ^ { d }$ represents model parameters (e.g., modelweights of a DNN) of dimension $d$ .

For an ML or DL problem, we typically take $f _ { i } ( w ) = \mathcal { L } ( x _ { i } , y _ { i } ; w )$ , which is the loss ofthe prediction on sample $( x _ { i } , y _ { i } )$ for the given model parameters $w$ , where $x _ { i }$ and $y _ { i }$ denote theith data point and the corresponding label, respectively.

Assume that there are $K$ participants (also known as data owners or clients) in an HFLsystem, with $\mathcal { D } _ { k }$ denoting the dataset owned by the $k$ th participant, with $\mathcal { P } _ { k }$ being the setof indexes of data points on client $k$ . Define $n _ { k } = | \mathcal { P } _ { k } |$ as the cardinality of $\mathcal { P } _ { k }$ . That is, it isassumed that the ith participant has $n _ { k }$ training data points. As a result, considering there are$K$ participants, Equation (4.2) can be rewritten as

$$
f (w) = \sum_ {k = 1} ^ {K} \frac {n _ {k}}{n} F _ {k} (w) \quad \text {w h e r e} \quad F _ {k} (w) = \frac {1}{n _ {k}} \sum_ {i \in \mathcal {P} _ {k}} f _ {i} (w). \tag {4.3}
$$

When the data points owned by the $K$ participants are independent and identically dis-tributed (IID), then we have $\mathbb { E } _ { \mathcal { D } _ { k } } \left[ F _ { k } ( w ) \right] = f ( w )$ , where the expectation $\mathbb { E } _ { \mathcal { D } _ { k } } \left[ \cdot \right]$ is taken overthe set of data points owned by the $k$ th participant. This IID assumption is typically made bydistributed optimization algorithms in DML paradigm. If the IID assumption does not hold,which is known as the non-IID setting described above, the loss function $F _ { k } ( \cdot )$ maintained atthe kth participant could be an arbitrarily bad approximation of the function $f ( \cdot )$ [Goodfellowet al., 2016, Zhao et al., 2018, Sattler et al., 2019].

SGD and its variants (e.g., mini-batch gradient descent) are the most popular optimiza-tion algorithms for DL [Zhang et al., 2019]. Many advances on DL can be understood as adapt-ing the structure of the model (and hence the loss function) to be more amenable to optimizationby simple gradient-based methods [Goodfellow et al., 2016, Zhang et al., 2019]. In light of thewidespread applications of DL, it is natural that we also develop new algorithms for federatedoptimization starting from SGD [McMahan et al., 2016b].

SGD can be applied naively to federated optimization, where a single mini-batch gradientcalculation (e.g., on a randomly selected subset of participants) is performed during each roundof federated training. Here, “one round” refers to the operations of sending updates from theparticipants to the server and from the server back to the participants, i.e., including the Steps1–4 of Figure 4.2. This approach is computationally efficient, but requires very large number ofcommunication rounds of training to produce satisfactory models, e.g., even using an advancedapproach like batch normalization (BN) [Ioffe and Szegedy, 2015] training on the MNISTdataset requires 50;000 rounds on mini-batches of size 60 [McMahan et al., 2016b].

For DML, with parallel training within data centers, or computing-clusters, communi-cation costs are relatively small, and computational costs dominate. Recent approaches focus onapplying graphics processing units (GPUs) to lower these costs. In contrast, in federated learn-ing, communication costs dominate as communication takes place over the Internet or wide areanetworks (WANs), even with wireless and mobile networks.

In federated learning, a single on-site dataset is usually small, compared to the total datasetsize, and modern terminals (such as smartphones) have relatively fast processors, even including

GPUs. As a result, computation cost is negligible compared to communication costs for manymodel types in federated learning. Hence, we may use additional computation to decrease thenumber of rounds of communication needed to train a model. The following are two primaryways to add computation [McMahan et al., 2016b].

• Increased parallelism. We can engage more participants working independently in be-tween client-server communication rounds.

• Increased computation on each participant. Rather than performing a simple computa-tion like a gradient calculation, each client performs a more complex calculation in betweencommunication rounds, such as performing multiple model weight update over a trainingepoch.

# 4.3.2 THE FEDAVG ALGORITHM

As articulated in McMahan et al. [2016b], the FedAvg algorithm family allows us to add com-putation using both approaches outlined above. The amount of computation is controlled bythree key parameters, namely: (1) $\rho$ , the fraction of clients that perform computation duringeach round; (2) S, the number of training steps each client performs over its local dataset duringeach round (i.e., the number of local epochs); and (3) $M$ , the mini-batch size used for the clientupdates. We use $M = \infty$ to indicate that the full local dataset is treated as a single mini-batch.

We may set $M = \infty$ and $S = 1$ to produce a form of SGD with a varying mini-batchsize. This algorithm selects a $\rho$ -fraction of participants during each round, and computes thegradient and the loss function over all the data held by these participants. Therefore, in thisalgorithm, $\rho$ controls the global batch size, with $\rho = 1$ corresponding to the full-batch gradientdescent using all data held by all participants. Since we still select batches by using all the data onthe chosen participants, we refer to this simple baseline algorithm as FederatedSGD. While thebatch selection mechanism is different from selecting a batch by choosing individual examplesuniformly at random, the batch gradients $g$ computed by the FederatedSGD algorithm stillsatisfy $\mathbb { E } [ g ] = \nabla f ( w )$ , provided that the datasets held at different participants are IID.

It is commonly assumed that the coordinator or server has the initial ML model, andthe participants know the settings of the optimizer. For a typical implementation of distributedgradient descent with a fixed learning rate $\eta$ , in the tth round of global model weight update,the $k$ th participant computes $g _ { k } = \nabla F _ { k } ( w _ { t } )$ , the average gradient on its local data points at thecurrent model weight $w _ { t }$ , and the coordinator aggregates these gradients and applies the updateof model weights according to McMahan et al. [2016b]:

$$
w _ {t + 1} \leftarrow w _ {t} - \eta \sum_ {k = 1} ^ {K} \frac {n _ {k}}{n} g _ {k}, \tag {4.4}
$$

where IID. $\begin{array} { r } { \sum _ { k = 1 } ^ { K } \frac { n _ { k } } { n } g _ { k } = \nabla f ( w _ { t } ) } \end{array}$ , provided that the data points he send the updated model weights different participants areback to the participants.$w _ { t + 1 }$


Algorithm 4.1 The FedAvg Algorithm (adapted from McMahan et al. [2016b])


1: The coordinator executes:  
2: Initialize model weight  $w_0$ , and broadcasts the initial model weight  $w_0$  to all participants.  
3: for each global model update round  $t = 1, 2, \ldots$  do  
4: The coordinator determines  $C_t$ , which is the set of randomly selected  $\max(K\rho, 1)$  participants.  
5: for each participant  $k \in C_t$  in parallel do  
6: Updates model weight locally:  $w_{t+1}^k \gets \text{Participant Update } (k, \overline{w}_t)$ .  
7: Sends the updated model weight  $w_{t+1}^k$  to the coordinator.  
8: end for  
9: The coordinator aggregates the received model weights, i.e., taking the weighted average of the received model weights:  $\overline{w}_{t+1} \gets \sum_{k=1}^{K} \frac{n_k}{n} w_{t+1}^k$   
10: The coordinator checks whether the model weights converge. If yes, then the coordinator signals the participants to stop.  
11: The coordinator broadcasts the aggregated model weights  $\overline{w}_{t+1}$  to all the participants.  
12: end for  
13: Participant Update  $(k, \overline{w}_t)$ :  
(This is executed by participant  $k$ ,  $\forall k = 1, 2, \ldots, K$ )  
14: Obtain the latest model weight from the server, i.e., set  $w_{1,i}^k = \overline{w}_t$   
15: for each local epoch  $i$  from 1 to number of epochs S do  
16: batches  $\gets$  randomly divides dataset  $D_k$  into batches of size  $M$ .  
17: Obtain the local model weight from last epoch, i.e., set  $w_{1,i}^k = w_{B,i-1}^k$   
18: for batch index  $b$  from 1 to number of batches  $B = \frac{n_k}{M}$  do  
19: Computing the batch gradient  $g_k^b$ .  
20: Updates model weights locally:  $w_{b+1,i}^k \gets w_{b,i}^k - \eta g_k^b$ .  
21: end for  
22: end for  
23: Obtains the local model weight update  $w_{t+1}^k = w_{B,S}^k$ , and sends it to the coordinator.

Alternatively, the coordinator can send the averaged gradients $\begin{array} { r } { \overline { { g } } _ { t } = \sum _ { k = 1 } ^ { K } \frac { n _ { k } } { n } g _ { k } } \end{array}$ back to the$w _ { t + 1 }$tion (4.4). This method is called gradient averaging [Tang et al., 2019, Su and Chen, 2018].

It is straightforward to show that an equivalent approach is given by [McMahan et al.,2016b]

$$
\forall k, w _ {t + 1} ^ {k} \leftarrow \overline {{w}} _ {t} - \eta g _ {k} \tag {4.5}
$$

$$
\bar {w} _ {t + 1} \leftarrow \sum_ {k = 1} ^ {K} \frac {n _ {k}}{n} w _ {t + 1} ^ {k}. \tag {4.6}
$$

That is, each client locally takes one step (or multiple steps) of gradient descent on the currentmodel weights $\overline { { w } } _ { t }$ using its local data according to Equation (4.5), and sends the locally updatedmodel weights $w _ { t + 1 } ^ { k }$ to the server. The server then takes a weighted average of the resultingmodels according to Equation (4.6), and sends the aggregated model weights $\overline { { w } } _ { t + 1 }$ back to theparticipants. This method is called model averaging [McMahan et al., 2016b, Yu et al., 2018].

The model averaging variant of the FedAvg algorithm is summarized in Algorithm 4.1.Once the algorithm is written in this way, it is natural to ask what happens when the participantiterates the local update (see Equation (4.5)) multiple times before going into the averaging step?For a participant with $n _ { k }$ local data points, the number of local updates per round is given by$\begin{array} { r } { u _ { k } = \frac { n _ { k } } { M } S . } \end{array}$ . The complete pseudo-code of the FedAvg algorithm with model averaging is givenin Algorithm 4.1.

However, for general non-convex objectives, model averaging in the model weight spacemay produce an arbitrarily bad model, and it may not even converge at all [Tang et al., 2019, Suand Chen, 2018]. Luckily, recent work indicates that in practice, the loss surfaces of sufficientlyover-parameterized DNNs are surprisingly well behaved, and in particular less prone to bad localminima than previously thought [Goodfellow et al., 2015]. When we start two models from thesame random initialization and then, again train each independently on a different subset ofthe data (as described above), it has been found out empirically that model averaging basedapproach works surprisingly well [McMahan et al., 2016a,b, Yu et al., 2018]. The success ofdropout training may provide some intuitions for the success of the federated model averagingscheme. Dropout training can be interpreted as averaging models of different architectures thatshare model weights, and the inference-time scaling of the model weights is analogous to themodel averaging used in Srivastava et al. [2014].

# 4.3.3 THE SECURED FEDAVG ALGORITHM

The plain FedAvg algorithm in the form of Algorithm 4.1 exposes plaintext intermediate results,such as gradients from an optimization algorithm like SGD or model weights of DNNs, tothe coordinator. No security guarantee is provided against the coordinator, and the leakage ofgradients or model weights may actually leak important data and model information [Phong etal., 2018] if the data structure is also exposed. We can leverage privacy-preserving techniques,


Algorithm 4.2 The Secured FedAvg Algorithm (model averaging with AHE)


1: The coordinator executes:  
2: Initialized model weight  $w_0$ , and broadcasts the initial model weight  $w_0$  to all participants.  
3: for each global model update round  $t = 1, 2, \ldots$  do  
4: The coordinator determines  $C_t$ , which is the set of randomly selected  $\max(K\rho, 1)$  participants.  
5: for each participant  $k \in C_t$  in parallel do  
6: Updates model weight locally:  $[[w_{t+1}^k]] \gets \text{Participant Update } (k, [[\overline{w}_t]])$ .  
7: Sends the updated model weight  $[[w_{t+1}^k]]$  and the corresponding loss  $\mathcal{L}_{t+1}^k$  to the coordinator.  
8: end for  
9: The coordinator aggregates the received model weights, i.e., taking the weighted average of the received model weights:  $[[\overline{w}_{t+1}]] \gets \sum_{k=1}^{K} \frac{n_k}{n} [[w_{t+1}^k]]$  (With slight abuse of notations for visual comfort, these are operations over ciphertexts, see, e.g., Paillier [1999].)  
10: The coordinator checks whether the loss  $\sum_{k \in C_t} \frac{n_k}{n} \mathcal{L}_{t+1}^k$  converges or the maximum number of rounds is reached. If yes, then the coordinator signals the participants to stop.  
11: The coordinator broadcasts the aggregated model weights  $[[\overline{w}_{t+1}]]$  to all the participants.  
12: end for  
13: Participant Update  $(k, [[\overline{w}_t]])$ :  
(This is executed by participant  $k$ ,  $\forall k = 1, 2, \ldots, K$ .)  
14: Decrypts  $[[\overline{w}_t]]$  to obtain  $\overline{w}_t$ .  
15: Obtain the latest model weight from the server, i.e., set  $w_{1,1}^k = \overline{w}_t$   
16: for each local epoch  $i$  from 1 to number of epochs S do  
17: batches  $\gets$  randomly divides dataset  $D_k$  into batches of size  $M$ .  
18: Obtain the local model weight from last epoch, i.e., set  $w_{1,i}^k = w_{B,i-1}^k$   
19: for batch index  $b$  from 1 to number of batches  $B = \frac{n_k}{M}$  do  
20: Computing the batch gradient  $g_k^b$ .  
21: Updates model weights locally:  $w_{b+1,i}^k \gets w_{b,i}^k - \eta g_k^b$ .  
22: end for  
23: end for  
24: Obtains the local model weight update  $w_{t+1}^k = w_{B,S}^k$ .  
25: Performs AHE on  $w_{t+1}^k$  to get  $[[w_{t+1}^k]]$ , and sends  $[[w_{t+1}^k]]$  and the corresponding loss  $\mathcal{L}_{t+1}^k$  to the coordinator.

such as the widely used methods described in Chapter 2, to ensure user privacy and data securityin FedAvg.

As an illustrative example, we use additively homomorphic encryption (AHE) [Acar etal., 2018] (e.g., the Paillier algorithm [Paillier, 1999] or the learning with errors- (LWE) basedencyption [Phong et al., 2018]) to enhance the security feature of the FedAvg algorithm.

Recall that AHE is a semi-homomorphic encryption algorithm that only supports theaddition and multiplication operations (i.e., additional homomorphism and multiplicative ho-momorphism [Paillier, 1999]). For ease of reference, we summarize here the key properties ofAHE. Let $[ [ u ] ]$ and $[ [ v ] ]$ denote the homomorphic encryption of $u$ and $v$ , respectively. WithAHE, the following holds (see Section 2.4.2):

• Addition: $D e c _ { s k } ( [ [ u ] ] \oplus [ [ v ] ] ) = D e c _ { s k } ( [ [ u + v ] ] )$ , where $^ { 6 6 } \mathrm { { \oplus } } ^ { \prime \mathrm { { p } } }$ may represent multiplicationof the ciphertexts (see, e.g., Paillier [1999]).

• Scalar multiplication: $D e c _ { s k } ( [ [ u ] ] \odot n ) = D e c _ { s k } ( [ [ u \cdot n ] ] )$ , where “ˇ” may represent takingthe power of $n$ of the ciphertext (see, e.g., Paillier [1999]).

Thanks to these two nice properties of AHE, we can directly apply AHE to the FedAvg algo-rithm to ensure security against the coordinator/server.

Specifically, by comparing Algorithm 4.1 with Algorithm 4.2, it can be observed that se-curity measures, such as AHE, can be easily added on top of the original FedAvg algorithmto provide secure federated learning. It was shown in Phong et al. [2018] that, under certainconditions, the secured FedAvg algorithm in Algorithm 4.2 leaks no information of the partici-pants to an honest-but-curious coordinator, provided that the underlying homomorphic encryp-tion scheme is chosen-plaintext attack (CPA) secure. In other words, Algorithm 4.2 ensureshonest-but-curious security against the coordinator. With AHE, the data and the model itselfare not transmitted in plaintext form. Hence, there is almost no possibility of leakage at the rawdata level. However, encyption and decryption operations will increase the computational com-plexity, and transmission of cyphertext will introduce extra communication overhead. Anotherdrawback of AHE is that polynomial approximations (e.g., using first-order Taylor approxima-tion for loss and gradient computations) need to be performed in order to evaluate nonlinearfunctions. As a result, there is a trade-off between accuracy and privacy. Security measures forthe FedAvg algorithm needs further studies.

# 4.4 IMPROVEMENT OF THE FEDAVG ALGORITHM

# 4.4.1 COMMUNICATION EFFICIENCY

In the implementation of the FedAvg algorithm, each participant needs to send a full modelweight update to the server during each round of federated training. As modern DNN modelscan easily have millions of parameters, sending model weights for so many values to a coor-dinator leads to huge communication costs, which grows with the number of participants and

iteration rounds. When there are a large number of participants, uploading model weights fromparticipants to the coordinator becomes the bottleneck of federated learning. To reduce com-munication costs, some methods are proposed to improve the communication efficiency. Oneexample is Konecný et al. [2016a], in which two strategies for computing model weights areproposed.

• Sketched updates. Participants compute a normal model weight update and perform acompression afterward locally. The compressed model weight update is often an unbiasedestimator of the true update, meaning they are the same on average. One possible way ofperforming model weight update compression is using probabilistic quantization. Partic-ipants then send the compressed updates to the coordinator.

• Structured updates. During the training process, the model weight update is restricted tobe of a form that allows for an efficient compression. For example, the model weight may beforced to be sparse or low-rank, or model weight update is computed within a restrictedspace that can be parameterized using a smaller number of variables. The optimizationprocess then finds the best possible update for this form.

Han et al. [2015] studied DNN model compression proposed a three-stage pipeline forcarrying out model weight compression. Firstly, prune the DNN connections by removing re-dundancy, keeping only the most meaningful connections. Secondly, the weights are quantizedso that multiple connections share the same weights, only effective weights are kept. Finally,Huffman coding is applied to take advantage of the biased distribution of effective weights.

When model weights are shared in federated learning, we can use model weight compres-sion to reduce communication costs. Similarly, when gradients are shared in federated learning,we can use gradient compression to bring down communication overhead. One well-knowngradient compression method is the deep gradient compression (DGC) approach [Kamp etal., 2018]. DGC employs four methods: namely (1) momentum correction, (2) local gradi-ent clipping, (3) momentum factor masking, and (4) warm-up training. Kamp et al. [2018]applied DGC on image classification, speech recognition, and language modeling tasks. Theresults showed that DGC can achieve a gradient compression ratio from 270–600 times with-out compromising model accuracy. Therefore, DGC can be employed to reduce communicationbandwidth required for sharing gradients or model weights and facilitate large-scale federatedDL or federated learning.

Besides compression, quantization is another efficient method for reducing communica-tion overhead in federated learning [Konecný et al., 2016a, Reisizadeh et al., 2019]. For example,the signSGD-based approach proposed in Chen et al. [2019] has very low per-iteration com-munication overhead, since it employs one-bit quantization per gradient dimension. Chen etal. [2019] developed a novel gradient correction mechanism that perturbs the local gradientswith noise and then applies one-bit quantization, which can also be seen as a special gradientcompression scheme.

It is also possible for clients to avoid uploading irrelevant model updates to the server,so as to reduce communication overhead, provided that the training convergence can still beguaranteed [Wang et al., 2019, Hsieh et al., 2017]. For example, Wang et al. [2019] proposed toprovide clients with the feedback information regarding the global tendency of model updating.Each client checks whether its local model update aligns with the global tendency and whetherit is relevant enough to global model improvement. In this way, each client can decide whetheror not it shall upload its local model update to the server. This can be seen as a special case ofclient selection.

# 4.4.2 CLIENT SELECTION

In the original work of McMahan et al. [2016b], client selection was recommended to reducecommunication cost and time taken for each global training round. However, no approach wasproposed for client selection. Nishio and Yonetani [2018] introduced a method for client selec-tion, which consists of two steps. The first step is the resource check step. That is, the coordinatorsends queries to a random number of participants to ask about their local resources and the size ofdata that are relevant to the training task. In the second step, the coordinator uses this informa-tion to estimate the time required for each participant to compute model weight update locally,and the time to upload the update. The coordinator then determines which participants to selectbased on these estimates. The coordinator wants to select as many participants as possible givena specific time budget for one global federated training round.

# 4.5 RELATED WORKS

The most recent Google workshop on federated learning brought together world-classresearchers and practitioners and presented the newest development of federated learn-ing [Google, 2019], such as agnostic federated learning [Mohri et al., 2019], federated transferlearning (see Chapter 6), the incentive mechanism design for federated learning (see Chapter 7),the privacy, security, and fairness aspects of federated learning (see, e.g., Agarwal et al. [2018],Pillutla et al. [2019], Melis et al. [2018], Ma et al. [2019]), as well as a lecture on using the open-source platform TensorFlow Federated [TFF, 2019] for research and deployment of federatedlearning. We review here some examples of the related studies.

Communication is one of the major challenges of federated learning. In Wang and Joshi[2019], an adaptive communication strategy, termed as AdaComm, was proposed to tackle theproblem of random communication delays encountered in federated learning. AdaComm firststarts with infrequent model averaging to save communication bandwidth and to deal withrandom delays, as well as to improve convergence speed. Then it increases the communica-tion frequency in order to achieve better model performance and a low error floor. Wang andJoshi [2019] presented theoretical analysis of the error-runtime trade-off for periodic-averagingSGD algorithm, where each participant performs local updates and their models are averagedperiodically (e.g., after every $\tau$ iterations). Wang and Joshi [2019] is the first work to analyze

the convergence of periodic-averaging SGD in terms of error with respect to wall-clock time,instead of the number of iterations, while taking into account the effect of computation andcommunication delays on the runtime per iteration. AdaComm is a communication-efficientSGD algorithm for federated learning, which is particularly suitable for mobile applications.

As was discussed in Section 4.3, while the FedAvg algorithm works well for certainnon-convex objective functions (also known as cost or loss functions) under IID settings, itcould produce unpredictable results for generally non-convex objective functions with non-IIDdatasets [Goodfellow et al., 2015]. In Xie et al. [2019], a new asynchronous solution was pro-posed to improve the flexibility and scalability of federated optimization with non-IID trainingdata. The key idea is that the server and the clients conduct model updates asynchronously. Theserver immediately updates the global model whenever it receives a local model from a client.The communication between the server and the clients is non-blocking. Xie et al. [2019] fur-ther analyzed the convergence of their proposed asynchronous approach for a restricted familyof non-convex problems under non-IID settings. It was also demonstrated with numerical ex-amples that the asynchronous algorithm enjoys fast convergence and tolerates staleness. Severalmixing hyperparameters are introduced to control the trade-off between the convergence rateand variance reduction according to the staleness. However, the hyperparameters of the pro-posed asynchronous algorithm could be difficult to tune in practice.

The coordinator in HFL is a potential privacy leak and some scholars actually prefer toremove the coordinator. For example, Zantedeschi et al. [2019] considered federated learningunder the peer-to-peer architecture, i.e., without the central coordinator, and proposed an opti-mization procedure that leverages a collaboration graph describing the relationships between thetasks of the participants. The collaboration graph and the ML models are jointly learned. Thefully decentralized solution of Zantedeschi et al. [2019] alternates between (i) training nonlinearML models given the graph in a greedy boosting manner, and (ii) updating the collaborationgraph (with controlled sparsity) when given the ML models. Further, the participants exchangemessages only with a small number of peers (their direct neighbors in the graph and a few morerandom participants), thus ensuring the scalability of this fully decentralized solution.

HFL was originally proposed and has been promoted by Google for B2C (business-to-consumer) applications, i.e., mainly for collaborative ML model training employing mobile de-vices [Konecný et al., 2016b, Yang et al., 2018, Hard et al., 2018], and especially for scenarioswith a large number of mobile devices [Bonawitz and Eichner et al., 2019]. While Google isadvocating and developing HFL for mobile applications, HFL has been applied to a varietyof practical scenarios, particularly to the B2B (business-to-business) applications. For instance,during the Google federated learning workshop [Google, 2019], Prof. Dawn Song from UCBerkeley, talked about applying federated learning for anomaly detection, such as fraud detec-tion [Song, 2019, Hynes et al., 2018], and there are several recent works along this direction,see, e.g., Nguyen et al. [2019] and Preuveneers et al. [2018]. Chapters 8 and 10 will providemore examples of practical applications of HFL.

# 4.6 CHALLENGES AND OUTLOOK

There are some examples of commercial deployment of HFL systems, such as the one carriedout by Google on mobile devices, i.e., the Gboard system [Bonawitz and Eichner et al., 2019].However, HFL is still in its infancy, and widespread adoption of HFL still faces numerouschallenges [Yang et al., 2019, Li, Wen, and He, 2019, Li et al., 2019]. Here, we briefly discusssome of the major challenges.

The first major challenge is the inability to inspect training data, which leads to one of thecentral problems, namely choosing the hyperparameters of an ML or DL model and setting theoptimizers, particularly for training DNN models. It is common to assume that the coordinatoror the server has the initial model and knows how to train the model. However, in practice, sincewe do not collect any data in advance, it is almost impossible to choose the right hyperparametersfor a DNN model and set up an optimizer beforehand. Here, the hyperparameters may includethe number of layers for a DNN, the number of nodes in each layer of a DNN, the structureof the convolutional neural networks (CNNs), the structure of the recurrent neural networks(RNNs), the output layer of a DNN, and the activation functions, etc. Optimizer options mayinclude which optimizer to use, batch sizes, and learning rates. For example, even the learningrate is difficult to determine since we have no information about the gradient magnitude ateach participant. Trying out many different learning rates in production would take time andcould worsen development experience. To address this challenge, the simulation based approachsuggested by Hartmann [2018, 2019] appears to be promising.

The second challenge is how to effectively motivate companies and organizations to par-ticipate in HFL. Traditionally, large companies and organizations have been trying to collectdata and create data silos so to be more competitive in the AI age. By joining HFL, other com-petitors may benefit from such large companies’ data, leading to these large companies losingmarket dominance. As a result, motivating the large companies to adopt HFL could be diffi-cult. To resolve this challenge, we need to devise effective data protection policies, appropriateincentive mechanisms, and business models for HFL.

When applied to mobile devices, it will also be difficult to convince the mobile deviceowners to allow for their devices to participate in federated learning. Sufficient incentives andbenefits shall be demonstrated to the mobile users to draw their interests in offering their mobiledevices to join in federated learning, such as potential for better user experience after joining infederated learning.

The third challenge is how to prevent cheating behaviors from participants. It is commonlyassumed that the participants are honest. However, in real-life scenarios, honesty only comesunder regulations and laws. For example, one participating party may fraudulently claim thenumber of data points it can contribute for model training and report false testing results of thetrained model, in order to gain more rewards. Since we are not able to inspect the datasets of anyparticipants, it is difficult to detect such cheating behaviors. To address this challenge, we needto design a holistic approach for protecting the rights and interests of the honest participants.

To realize the full potential HFL, much research is still needed. In addition to addressingthe aforementioned challenges, we need to study mechanisms for managing the training pro-cess. For example, since model training and evaluation are carried out locally at each participant,we need to develop new ways to avoid over-fitting and to trigger early-stopping. Another in-teresting direction is how to handle participants with different reliability levels. For example,some participants may leave during the training process of HFL due to interrupted networkconnections or other issues. As a result, we need smart solutions to replace the dropped partici-pants with new participants without affecting the training process and model accuracy, especiallywithout affecting the convergence speed of model training. Finally, we need to develop efficientmechanisms to defend against model poisoning attacks (such as targeted backdoor attacks) infederated learning systems.

# Vertical Federated Learning

We learned from Chapter 4 that horizontal federated learning (HFL) is applicable to scenar-ios where participants’ datasets share the same feature space but differ in sample spaces. Thus,HFL is convenient to be applied to build applications powered by a massive amount of mobiledevices [McMahan et al., 2016a, McMahan and Ramage, 2017]. In those cases, the targetsbeing federated are the individual consumers of applications, which can be considered as B2C(business-to-consumer) paradigm. However, in many practical scenarios, the participants of fed-erated learning are organizations that collected different data features for the same group of peo-ple for pursuing different business goals. Those organizations often have strong motivations tocooperate to improve business efficiency, which can be considered as B2B (business-to-business)paradigm.

For example, assume that there is a user has some records in a bank that reflect the user’srevenue, expenditure behavior and credit rating. Also, the same user has some other informationstored in a e-commerce marketplace retaining the user’s online browsing and purchasing history.Although the feature spaces of the two organizations are quite different, they have a close as-sociation with each other. For instance, the user’s purchasing history may somewhat determinethe user’s credit rating. Such scenarios are common in real life. Retailers may partner with banksto offer personalized services or products based on the purchasing history and the expenditurebehavior of the same user. Hospitals can collaborate with pharmaceutical companies to makeuse of the medical records of common patients so as to treat chronic diseases and to reduce risksof future hospitalization.

We categorize federated learning on participants whose datasets share the same samplespace but differ in feature space as Vertical Federated Learning (VFL). The word “vertical” comesfrom the term “vertical partition,” which is widely used in the context of the traditional tabularview of a database (e.g., columns of a table are vertically partitioned into different groups andeach column represents a feature of all samples). In this chapter, we introduce VFL, covering itsconcept, architecture, algorithms, and open research challenges.

# 5.1 THE DEFINITION OF VFL

The datasets maintained by different organizations having different business goals usually havedifferent feature spaces, while those organizations may share a large pool of common users.This is illustrated in Figure 5.1. With VFL, also called feature-partitioned federated learning,we can leverage the heterogeneous feature spaces of distributed datasets maintained by those

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/adff90c9c1de637355b019654101be75200eafe7d67737faea79bc62689d8998.jpg)



Figure 5.1: Illustration of VFL, a.k.a., feature-partitioned federated learning [Yang et al., 2019].


organizations to build better machine learning (ML) models without exchanging and exposingthe private data.

Under the federated learning framework, the identity and the status of each participatingparty is the same, and the federation helps everyone establish a “commonwealth” strategy, whichis why this is called “federated learning.” For such a VFL system, we have:

$$
\mathcal {X} _ {i} \neq \mathcal {X} _ {j}, \mathcal {Y} _ {i} \neq \mathcal {Y} _ {j}, I _ {i} = I _ {j} \forall \mathcal {D} _ {i}, \mathcal {D} _ {j}, i \neq j, \tag {5.1}
$$

where $\mathcal { X }$ and $\mathcal { V }$ denote the feature space and the label space, respectively. $I$ is the sample IDspace, and matrix $\mathcal { D }$ represents the data held by different parties [Yang et al., 2019]. The objectivefor all parties is to collaboratively build a shared ML model by exploiting all features collectedby participating parties.

In VFL settings, there are several underlying assumptions for achieving security and pre-serving privacy. First, it is assumed that the participants are honest-but-curious. This meansthat the participants attempt to deduce as much as possible from the information received fromother participants, although they abide by the protocol without disturbing it in any way. Sincethey also intend to build a more accurate model, they do not collude with one another. Second,it is assumed that the information transmission process is safe and reliable enough to defendagainst attacks. It is further assumed that the communication is lossless without tampering withthe intermediate results. A semi-honest third party (STP) may also join the participants to assistthe two parities. The STP is independent from both of the two parties. The STP collects theintermediate results to compute the gradients and loss, and distributes the results to each party.The information that the STP receives from the participants is either encrypted or obfuscated.The participants’ raw data are not exposed to each other, and each participant only receives themodel parameters related to its own features.

Security definition of a VFL system. A VFL system typically assumes honest-but-curious participants. In a two-party case, for example, the two parties are non-colluding andat most one of them are compromised by an adversary. The security definition is that the ad-versary can only learn data from the party that it corrupted but not data from the other partybeyond what is revealed by the input and output. To facilitate the secure computations betweenthe two parties, sometimes a STP is introduced, in which case it is assumed that STP does notcollude with either party. MPC provides formal privacy proof for these protocols [Goldreich etal., 1987]. At the end of learning, each party only holds the model parameters associated withits own features, therefore at inference time, the two parties also need to collaborate to generateoutput.

# 5.2 ARCHITECTURE OF VFL

For ease of elaboration, we use an example to describe the architecture of VFL. Suppose thatCompanies A and B would like to jointly train an ML model. Each of them has their own data.In addition, B also has labeled data that the model needs to perform prediction tasks. For userprivacy and data security reasons, A and B cannot directly exchange data. In order to ensure dataconfidentiality during the training process, a third-party collaborator C can be involved. Here,we assume that C is honest and does not collude with A or B, but A and B are honest-but-curious. The trusted third-party C is a legitimate assumption since the role of C can be playedby authorities such as governments or replaced by secure computing nodes such as Intel SoftwareGuard Extensions (SGX) [Bahmani et al., 2017]. An example of vertical federated learning ar-chitecture is illustrated in Figure 5.2a [Yang et al., 2019, Liu et al., 2019]. The training process ofa VFL system typically consists of two parts. It first establishes alignment between entities shar-ing the same IDs of two parities. Then, the encrypted (or privacy-preserving) training processis conducted on those aligned entities.

Part 1: Encrypted entity alignment. Since the user groups of the two companies A andB are not the same, the system uses an encryption-based user ID alignment technique suchas Liang and Chawathe [2004] and Scannapieco et al. [2007] to confirm the common usersshared by both parties without A and B exposing their respective raw data. During entity align-ment, the system does not expose users who belongs to only one of the two companies, as shownin Figure 5.3.

Part 2: Encrypted model training. After determining the common entities, we can usethese common entities’ data to train a joint ML model. The training process can be divided intothe following four steps (as illustrated in Figure 5.2b).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/a5605bb036af0c9dbb147da3ce218cc034776d5c71a640ec87f510dad515213e.jpg)



Figure 5.2: Architecture for a vertical federated learning system [Yang et al., 2019].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/aa58c13e76d39079b473a5c0d99630f33163a2c72ec241416ed5fbf70539d4b8.jpg)



Figure 5.3: Illustration of encrypted entity alignment [Cheng et al., 2019].


• Step 1: C creates encryption pairs, and sends the public key to A and B.

• Step 2: A and B encrypt and exchange the intermediate results for gradient and loss cal-culations.

• Step 3: A and B compute encrypted gradients and add an additional mask, respectively. Balso computes the encrypted loss. A and B send encrypted results to C.

• Step 4: C decrypts gradients and loss and sends the results back to A and B. A and Bunmask the gradients, and update the model parameters accordingly.

# 5.3 ALGORITHMS OF VFL

In this section, we elaborate two VFL algorithms to help the readers better understand howVFL works.

# 5.3.1 SECURE FEDERATED LINEAR REGRESSION

The first algorithm is federated linear regression, which was first presented in Yang et al. [2019].This algorithm exploits homomorphic encryption to protect the privacy of local data belongingto each participating party during the training process of the federated linear regression model.For ease of reference, the notations used in this section are summarized in Table 5.1.


Table 5.1: Notations


<table><tr><td>η</td><td>The learning rate</td></tr><tr><td>λ</td><td>The regularization parameter</td></tr><tr><td>yi</td><td>The label space of party B</td></tr><tr><td>xia,xbi</td><td>Feature space of party A and B, respectively</td></tr><tr><td>ΘA, ΘB</td><td>Local model parameters of party A and B, respectively</td></tr><tr><td>uia</td><td>Defined as uiA= ΘAxia</td></tr><tr><td>ubi</td><td>Defined as uiB= ΘBxiB</td></tr><tr><td>[ [di]]</td><td>Defined as [[di]] = [[uiA]] + [[uiB - yi]]</td></tr><tr><td>{xiA}i∈DA</td><td>The local dataset of party A</td></tr><tr><td>{xiB, yi}i∈DB</td><td>The local dataset and labels of party B</td></tr><tr><td>[ [·]]</td><td>Additive homomorphic encryption (AHE)</td></tr><tr><td>RAand RB</td><td>The random masks of party A and party B, respectively</td></tr></table>

To train a linear regression model with gradient descent methods, we need a secure wayto compute the model loss and gradients. Given a learning rate $\eta$ , a regularization parameter $\lambda$ ,a dataset $\{ x _ { i } ^ { A } \} _ { i \in { \mathcal { D } } _ { A } }$ , $\{ x _ { i } ^ { B } , y _ { i } \} _ { i \in \mathcal { D } _ { B } }$ , and model parameters $\Theta _ { A }$ , $\Theta _ { B }$ corresponding to the featurespace of $x _ { i } ^ { A }$ , $x _ { i } ^ { B }$ , respectively, the training objective can be written as:

$$
\min  _ {\Theta_ {A}, \Theta_ {B}} \sum_ {i} \left\| \Theta_ {A} x _ {i} ^ {A} + \Theta_ {B} x _ {i} ^ {B} - y _ {i} \right\| ^ {2} + \frac {\lambda}{2} \left(\| \Theta_ {A} \| ^ {2} + \| \Theta_ {B} \| ^ {2}\right). \tag {5.2}
$$

# 74 5. VERTICAL FEDERATED LEARNING

Let $u _ { i } ^ { A } = \Theta _ { A } x _ { i } ^ { A }$ , $u _ { i } ^ { B } = \Theta _ { B } x _ { i } ^ { B }$ , the encrypted loss is:

$$
[ [ \mathcal {L} ] ] = \left[ \left[ \sum_ {i} \left(\left(u _ {i} ^ {A} + u _ {i} ^ {B} - y _ {i}\right)\right) ^ {2} + \frac {\lambda}{2} \left(\left\| \Theta_ {A} \right\| ^ {2} + \left\| \Theta_ {B} \right\| ^ {2}\right) \right] \right], \tag {5.3}
$$

where the additive homomorphic encryption operation is denoted as ŒŒ. Let $[ [ { \mathcal { L } } _ { A } ] ] =$$\begin{array} { r } { [ [ \sum _ { i } ( u _ { i } ^ { A } ) ^ { 2 } + \frac { \lambda } { 2 } | | \Theta _ { A } | | ^ { 2 } ] ] , [ [ \mathcal { L } _ { B } ] ] \stackrel { \circ } { = } [ [ \sum _ { i } ( u _ { i } ^ { \overleftarrow { B } } - y _ { i } ) ^ { 2 } + \frac { \lambda } { 2 } | | \Theta _ { B } | | ^ { 2 } ] ] } \end{array}$ , and $\begin{array} { r } { [ [ \mathcal { L } _ { A B } ] ] = 2 \sum _ { i } [ [ u _ { i } ^ { A } ( u _ { i } ^ { B } - } \end{array}$$y _ { i } ) ] ]$ , then

$$
[ [ \mathcal {L} ] ] = [ [ \mathcal {L} _ {A} ] ] + [ [ \mathcal {L} _ {B} ] ] + [ [ \mathcal {L} _ {A B} ] ]. \tag {5.4}
$$

Similarly, let $[ [ d _ { i } ] ] = [ [ u _ { i } ^ { A } ] ] + [ [ u _ { i } ^ { B } - y _ { i } ] ]$ . Then, the gradients of the loss function withrespect to the training parameters are given by

$$
\left[ \left[ \frac {\partial \mathcal {L}}{\partial \Theta_ {A}} \right] \right] = 2 \sum_ {i} \left[ \left[ d _ {i} \right] \right] x _ {i} ^ {A} + \left[ \left[ \lambda \Theta_ {A} \right] \right] \tag {5.5}
$$

$$
\left[ \left[ \frac {\partial \mathcal {L}}{\partial \Theta_ {B}} \right] \right] = 2 \sum_ {i} \left[ \left[ d _ {i} \right] \right] x _ {i} ^ {B} + \left[ \left[ \lambda \Theta_ {B} \right] \right]. \tag {5.6}
$$

Note that party A and party B are able to compute $u _ { i } ^ { A }$ and $u _ { i } ^ { B }$ using only their respectivelocal information. However, the term $d _ { i }$ involves both $u _ { i } ^ { A }$ and $u _ { i } ^ { B } - y _ { i } .$ It cannot be computedby either party alone. As a result, party A and party B should collaboratively compute $d _ { i }$ whilepreserving the privacy of $u _ { i } ^ { A }$ and $u _ { i } ^ { B } - y _ { i }$ against the other party. In the homomorphic encryp-tion setting, to prevent party A and party B from peeking into $u _ { i } ^ { B } - y _ { i }$ and $u _ { i } ^ { A }$ , respectively,$u _ { i } ^ { B } - y _ { i }$ and $u _ { i } ^ { A }$ are encrypted via the public key held by a third party C. The third party C inthe loop is mainly response for decrypting encrypted information passed from party A and partyB, and orchestrating the training and inference processes.

Introducing a third party into the loop is not always feasible to many practical scenarioswhere the legitimacy and accountability of the third party are hard to be guaranteed. Securemulti-party computation techniques such as secret sharing can be applied to remove the thirdparty and decentralize federated learning. We refer interested readers to Mohassel and Zhang[2017] for details. Here, we continue the elaboration with the architecture having a third party.

# The Training Process

We summarize the detailed steps of training the federated linear regression model in Table 5.2.During entity alignment and model training, data owned by parties A and B are stored locally,and the interactions in model training do not lead to data privacy leakage. Note that potentialinformation leakage to party C may or may not be considered to be privacy violation since partyC is a trusted party. To further prevent party C from learning information about parties A or Bin this case, parties A and B can further hide their gradients from party C by adding encryptedrandom masks.


Table 5.2: Training steps for secure linear regression


<table><tr><td></td><td>Party A</td><td>Party B</td><td>Party C</td></tr><tr><td>Step 1</td><td>Initializes ΘA</td><td>Initializes ΘB</td><td>Creates an encryption key pair and sends public key to A and B</td></tr><tr><td>Step 2</td><td>Computes [[uiA]], [[L_A]] and sends to B</td><td>Computes [[uiB]], [[diB]], [[L]], and sends [[diB]] to A, and sends [[L]] to C</td><td></td></tr><tr><td>Step 3</td><td>Initializes RA, com- putes [[∂L/∂θA]] + [[RA]] and sends to C</td><td>Initializes RB, com- putes[∂L/∂θB] + [RB] and sends to C</td><td>Decrypts [[L]] and sends [∂L/∂θA] + RA to A, [∂L/∂θB] + RB to B</td></tr><tr><td>Step 4</td><td>Updates ΘA</td><td>Updates ΘB</td><td></td></tr><tr><td>What is obtained?</td><td>ΘA</td><td>ΘB</td><td></td></tr></table>

The training protocol shown in Table 5.2 does not reveal any information to C, becauseall C learns are the masked gradients, and the randomness and secrecy of the masked matrix areguaranteed [Du et al., 2004]. In the above protocol, party A learns its gradient at each step, butthis is not enough for A to learn any information about B according to Equation (5.5), becausethe security of scalar product protocol is well-established based on the inability of definitivelysolving for more than n unknowns with only $n$ equations [Du et al., 2004, Vaidya and Clifton,2002]. Here, we assume the number of samples $N _ { A }$ is much greater than $n _ { A }$ , where $n _ { A }$ is thenumber of features. Similarly, party B cannot learn any information about A. Therefore, thesecurity of the protocol is proven.

Note that we have assumed both parties to be semi-honest. If a party is malicious andcheats the system by faking its input, for example, party A submits only one non-zero samplewith only one non-zero feature, it can tell the value of $u _ { i } ^ { B }$ for that feature of that sample. It stillcannot compromise $x _ { i } ^ { B }$ or $\Theta _ { B }$ though, and the deviation will distort results for the next iteration,thereby alerting the other party who can then terminate the learning process in response. At theend of the training process, each party remains oblivious about the data structure of the otherparty, and it obtains the model parameters associated only with its own features.

Because the loss and gradients each party receives are exactly the same as the loss andgradients they would receive if jointly building a model with data gathered at one place withoutprivacy constraints, this collaboratively trained model is lossless and its optimality is guaranteed.

The efficiency of the model depends on the communication overhead and the computationoverhead incurred for encrypting the data. In each iteration, the information sent between A and

B increases with the number of overlapping samples. Therefore, the efficiency of this algorithmcan be further improved by adopting distributed parallel computing techniques.

# The Inference Process

At inference time, the two parties need to collaboratively compute the inference results, as thesteps summarized in Table 5.3. During inference, the data belonging to each party would notbe exposed to the other.


Table 5.3: Inference steps for secure linear regression


<table><tr><td></td><td>Party A</td><td>Party B</td><td>Evaluator C</td></tr><tr><td>Step 0</td><td></td><td></td><td>Sends user ID i to A and B</td></tr><tr><td>Step 1</td><td>Computes uA i and sends to C</td><td>Computes uB i and sends to C</td><td>Computes the result of uA + uB</td></tr></table>

# 5.3.2 SECURE FEDERATED TREE-BOOSTING

The second example is secure federated tree-boosting (termed as SecureBoost for short), whichwas first studied in Cheng et al. [2019], in the setting of VFL. This work proves that SecureBoostis as accurate as other non-federated gradient tree-boosting algorithms that require data beingcollected at one central place. That is, SecureBoost provides the same level of accuracy as its non-privacy-preserving variants, while at the same time, reveals no information about each privatedata owner. Note that, in the description of this example, the coordinator corresponds to theso-called active party originally defined in Cheng et al. [2019], which has both data and labels.

# Secure Entity Alignment

Similar to federated secure linear regression described in Section 5.3.1, SecureBoost consists oftwo major steps. First, it aligns the data under the privacy constraint. Second, it collaborativelylearns a shared gradient-tree boosting model, while keeping all the training data secret overmultiple private parties.

The first step in the SecureBoost framework is entity alignment, which is to find a commonset of data samples (i.e., the common users) among all participating parties so as to build ajoint ML model. When the data are vertically partitioned over multiple parties, different partieshold different but partially overlapping users’ data. The common users may be identified bytheir unique user IDs. In particular, we can align the data samples under an encryption schemeby using the privacy-preserving protocol for inter-database intersections, see, e.g., Liang andChawathe [2004].

# Review of XGBoost

After aligning the data across different parties under the privacy constraints, we now considerthe problem of jointly building the tree ensemble model over multiple parties without violat-ing privacy through VFL. To achieve this goal, there are three key questions that need to beanswered.

• How can each party compute an updated model based on its local data without referenceto class labels?

• How can the coordinator aggregate all the updated models and obtain a new global model?

• How to share the updated global model among all parties without leaking any privateinformation at the inference time?

To help find answers to these questions, we first take a quick review of the tree ensemble model,XGBoost [Chen and Guestrin, 2016], in the non-federated setting.

Given a data set $\mathbf { X } \in \mathbb { R } ^ { n \times d }$ with $n$ samples and $d$ features, XGBoost predicts the outputby using $K$ regression trees:

$$
\hat {y} _ {i} = \sum_ {k = 1} ^ {K} f _ {k} \left(\mathbf {x} _ {i}\right), \forall \mathbf {x} _ {i} \in \mathbb {R} ^ {d}, i = 1, 2, \dots , n. \tag {5.7}
$$

To avoid bogging down into the mathematical details of tree boosting, we bypass thederivation of the loss function for learning the set of regression trees used in Equation (5.7).Instead, we introduce the training rules with pain words, hoping that it is more accessible. Theobjective of learning the regression tree ensemble is to find a best set of trees that provides smallclassification loss, as well as low model complexity. In gradient tree boosting, this objective isapproached by optimizing the loss (e.g., squared loss or Taylor approximation of a loss function)between label and prediction iteratively. In each iteration, we try to add a new tree that reducesthe loss as much as possible while do not introduces much complexity. Hence, the objectivefunction at tth iteration can be written as

$$
\min  \sum_ {i = 1} ^ {n} \left[ g _ {i} f _ {t} \left(\mathbf {x} _ {i}\right) + \frac {1}{2} h _ {i} f _ {t} ^ {2} \left(\mathbf {x} _ {i}\right) \right] + \Omega \left(f _ {t}\right), \tag {5.8}
$$

where $g _ { i }$ and $h _ { i }$ are two groups of independent variables, and $\Omega ( f _ { t } )$ are the complexity of thenew tree. This indicates that we only need to find a new tree that can optimize this objectivefunction, and it should be easy to find a optimal tree given this objective function with theoptimal score noted as $o b j _ { t }$ .

Hence, the construction of a newly added regression is a process to build a tree that min-imize $o b j _ { t }$ , i.e., from the depth of 0, deciding the split of each leaf node until reaching the max-imum depth. Now the question lays on how to decide a optimal split of a leaf node at each level

of the tree. The performance of a “split” is measured by the split gain, which can be calculatedfrom the aforementioned variables $g _ { i }$ and $h _ { i }$ . We have the following observations.

(i) The evaluation of split candidates and the calculation of the optimal weight of a leaf nodeonly depend on the variables $g _ { i }$ and $h _ { i }$ .

(ii) The class label is needed for the calculation of $g _ { i }$ and $h _ { i }$ , and is easy to recover the classlabel from $g _ { i }$ and $h _ { i }$ once we obtain the value of $y _ { i } ^ { ( t - 1 ) }$ from the $( t - 1 )$ th iteration.


Algorithm 5.1 Aggregate Dencrypted Gradient Statistics (adapted from Cheng et al. [2019])


Input:  $I$  , the instance space of the current node;   
Input:  $d$  , feature dimension;   
Input:  $\{[[g_i]],[[h_i]]\} _i\in I$    
Output:  $\mathbf{G}\in \mathbb{R}^{d\times l}$ $\mathbf{H}\in \mathbb{R}^{d\times l}$  1: for  $k = 0\rightarrow d$  do 2: Propose  $S_{k} = \{s_{k1},s_{k2},\dots,s_{kl}\}$  by percentiles on feature  $k$  3: end for 4: for  $k = 0\rightarrow d$  do 5:  $\mathbf{G}_{kv} = \sum_{i\in \{i|s_{k,v}\geq x_{i,k} > s_{k,v - 1}\}}[[g_i]]$  6:  $\mathbf{H}_{kv} = \sum_{i\in \{i|s_{k,v}\geq x_{i,k} > s_{k,v - 1}\}}[[h_i]]$  7: end for

# The Training Process of SecureBoost

We know from the above observations that each party can determine the local optimal splitindependently with only its local data once it obtains $g _ { i }$ and $h _ { i }$ . The optimal split can be foundif the split gain can be calculated for every possible splits, by using the sum of groups of $g _ { i }$ andh i . $h _ { i }$

In order to keep $g _ { i }$ and $h _ { i }$ confidential to avoid privacy leakage, $g _ { i }$ and $h _ { i }$ shall be en-crypted before being sent to the other parties. As an example, we show here how to calculatethe candidate split gain with encrypted $g _ { i }$ and $h _ { i }$ using the additive homomorphic encryptionscheme [Paillier, 1999].

With the additive homomorphic encryption scheme, the split gain for every split candi-date can be computed by the sum of groups of ciphertexts of $g _ { i }$ and $h _ { i }$ , respectively. Therefore,the best split at each party can be found by evaluating all the possible split gains in the coordi-nator that can hence apply a global optimal split.

However, this solution is not efficient since it requires the transmission for all possiblesplit candidates, which incurs enormous communication overhead. To construct a boosting-treewith lower communication cost, we can take advantage of the approximate framework proposedin Chen and Guestrin [2016], where the detailed calculation is shown in Algorithm 5.1.


Algorithm 5.2 Find Optimal Split (adapted from Cheng et al. [2019])


Input: I, instance space of current node  
Input:  $\{\mathbf{G}^i,\mathbf{H}^i\}_{i = 1}^m$  , aggregated encrypted gradient statistics from  $m$  parties  
Output: Partition current instance space according to the selected attribute's value

1: The Coordinator executes:

2: $\begin{array} { r } { g  \sum _ { i \in I } g _ { i } , \quad h  \sum _ { i \in I } h _ { i } } \end{array}$

3: Enumerate over all parties:

4: for $i = 0 \to m$ do

5: Enumerate over all features

6: for $k = 0  d _ { i }$ do

7: $g _ { l } \gets 0 , h _ { l } \gets 0$

8: // Enumerate over all threshold value

9: for $v = 0 \to l _ { k }$ do

10: Get decrypted values $D ( \mathbf G _ { k v } ^ { i } )$ and $D ( \mathbf { H } _ { k v } ^ { i } )$

11:

12:

g 213:

14: end for

15: end for

16: end for

17: Return $k _ { o p t }$ and ${ \boldsymbol { v } } _ { o p t }$ to the corresponding party $i$ when we obtain the max score.

18: Party i executes (for many parties in parallel):

19: Determine the selected attribute’s value according to $k _ { o p t }$ and ${ \boldsymbol { v } } _ { o p t }$ and partition currentinstance space.

20: Record the selected attribute’s value and return [record id, IL] back to the collaborator.

21: The Coordinator executes:

22: Split current node according to $I _ { L }$ and associate current node with [party id, record id].

With Algorithm 5.1, for each party, instead of computing $[ [ g _ { l } ] ]$ and $[ [ h _ { l } ] ]$ directly, it mapsthe features into buckets and then aggregates the encrypted gradient statistics based on thebuckets. In this way, the coordinator only needs to collect the aggregated encrypted gradientstatistics from all parties. As a result, it can determine the globally optimal split more efficiently,as described in Algorithm 5.2.

After the coordinator obtains the global optimal split, represented as Œ party id $( i )$ , featureid $( k )$ , threshold id $\left( v \right) ]$ , it returns the feature id $k$ and threshold id $v$ to the corresponding party

i . Party $i$ decides the value of the selected attribute based on the values of $k$ and $v$ . Then, itpartitions the current instance space according to the value of the selected attribute. In addition,it builds a lookup table locally to record the value of the selected attribute, [feature, thresholdvalue]. After that, it returns the index of the record and the instance space of left side nodesafter the split $\left( I _ { L } \right)$ back to the active party. The active party splits the current node accordingto the received instance space and associates the current node with [party id, record id], untila stopping criterion or the maximum depth is reached. All the leaf nodes are stored inside theactive party.

In summary, the step-by-step training process of SecureBoost can be concluded as follows.

• Step 1: Starting from the active party, it first calculates $g _ { i }$ and $h _ { i }$ , $i \in \{ 1 , \ldots , N \}$ , andencrypts it using AHE.

• Step 2: The active party generates encrypted buckets according to Algorithm 5.1 and sendthem to all passive parties.

• Step 3: For each passive party, it maps the features into buckets and then aggregates theencrypted gradient statistics based on the buckets. The results are sent to the active party.

• Step 4: The active party decrypts the aggregated result, and determines the global optimalsplit according to Algorithm 5.2, and returns $k _ { o p t }$ and ${ { v } _ { o p t } }$ to the corresponding passiveparty.

• Step 5: The passive party determines the attribute’s value according to $k _ { o p t }$ and ${ { v } _ { o p t } }$ receivedfrom the active party, and returns the corresponding records to the active party.

• Step 6: Repeat Steps 2–4 iteratively until the maximum score is reached.

# The Inference Process of SecureBoost

For federated model inference, we are able to classify a new sample even though its features areprivately distributed on different parties. Since all leaf nodes are stored in the active party, theinference process should be coordinated by the active party with the information from otherpassive parties, which have party-specific lookup table consisting of [feature, threshold value].The inference process is simply recursive steps as follows.

• Step 1: The active party refers to the owner (i.e., party-id) of the root node with the relatedfeature-threshold tuple (i.e., record-id).

• Step 2: The retrieved party compare the value of the corresponding attribute with thethreshold from the lookup table, and decide which child node to retrieve.

• Step 3: The active party returns the party-id and record-id of the retrieved node.

• Step 4: Repeat Step 2 until a leaf node is reached.

In each step, the active party only reacts to the retrieval of node-id and correspondingparty-id and record-id. And the actual attribute values are only exposed to the parties that ownscorresponding attribute values. Therefore, the federated inference is not only private but alsolossless.

# 5.4 CHALLENGES AND OUTLOOK

VFL enables participants to build a shared model based on data with heterogeneous features in aprivacy-preserving manner. Unlike HFL in which a common model is shared by all participants,in VFL the model is partitioned into multiple components each maintained by a participantwith relevant but different data features. Thus, participants in VFL have a closer interdependentrelationship with each other. More specifically, the training of each model component mustfollow a certain computation order specified by the underlying VFL algorithm. In other words,participants have dependent computations and need to frequently interact with each other toexchange the intermediate results.

Therefore, VFL is vulnerable to communication failures and thus requires reliable and ef-ficient communication mechanisms. Transferring the intermediate results from one participantto another can be expensive, as long-haul connections must be established between two par-ticipants located in different geographical regions. Such slow data transfer, in turn, results ininefficient utilization of computing resources, as a participant cannot start training until it hasreceived all the required intermediate results. To address this issue, we may need to design astreaming communication mechanism that can judiciously schedule the training and commu-nication of each participant to offset the data transfer delay. A fault-tolerant mechanism shouldalso be designed to prevent the VFL process from crashing in the middle of training.

Currently, on the setting of federated learning, most works proposed to reduce informa-tion leakage or prevent malicious attacks are applied in HFL. As VFL typically requires a closerand more direct interaction between participants, flexible secure protocols that can meet securerequirements of each participant are needed. Previous works [Baldimtsi et al., 2018, Bost et al.,2015] have demonstrated that different secure tools are optimal for different types of computa-tions, e.g., garbled circuits give efficient comparisons whereas secret sharing and homomorphicencryption yield efficient arithmetic function evaluation. We may explore hybrid strategies forconversion among secure techniques, aiming to achieve locally optimal performance for eachpart of the computation. In addition, efficient secure entity alignment is also worth being ex-plored since it is a crucial preprocessing component of VFL.

# Federated Transfer Learning

We have discussed horizontal federated learning (HFL) and vertical federated learning (VFL)in Chapters 4 and 5, respectively. HFL requires all participating parties share the same featurespace while VFL require parties share the same sample space. In practice, however, we oftenface situations in which there are not enough shared features or samples among the participat-ing parties. In those cases, one can still build a federated learning model combined with transferlearning that transfers knowledge among the parties to achieve better performance. We referto the combination of federated learning and transfer learning as Federated Transfer Learn-ing (FTL). In this chapter, we provide a formal definition of FTL and discuss the differencesbetween FTL and traditional transfer learning. We then introduce a secure FTL frameworkproposed in Liu et al. [2019], and conclude this chapter with a summary of the challenges andopen issues.

# 6.1 HETEROGENEOUS FEDERATED LEARNING

Both HFL and VFL require all participants share either the same feature space or the same sam-ple space in order to build an effective shared machine learning (ML) model. In more practicalscenarios, however, datasets maintained by participants may be highly heterogeneous in one wayor the other.

• Datasets may share only a handful of samples and features.

• Distributions among those datasets could be quite different.

• The size of those datasets could vary greatly.

• Some participants may only have data with no or limited labels.

To address these issues, federated learning can be combined with transfer learning tech-niques [Pan and Yang, 2010] to enable a broader range of businesses and applications that haveonly small data (few overlapping samples and features) and weak supervision (few labels) to buildeffective and accurate ML models while complying with data privacy and security law [Yanget al., 2019, Liu et al., 2019]. We refer to the combination of federated learning and transferlearning as FTL, which deals with problems that exceed the scope of the existing HFL andVFL settings.

# 6.2 FEDERATED TRANSFER LEARNING

Transfer learning is a learning technique to provide solutions for cross-domain knowledge trans-fer. In many applications, we only have a small amount of labeled data or weak supervision suchthat ML models cannot be built reliably [Pan and Yang, 2010]. In such situations, we can stillbuild high-performance ML models by leveraging and adapting models from similar tasks ordomains. In recent years, there have been an increasing number of research works on applyingtransfer learning to various fields ranging from image classification [Zhu et al., 2011] to naturallanguage understanding and sentiment analysis [Li et al., 2017, Pan et al., 2010].

The essence of transfer learning is to find the invariant between a resource-rich source do-main and a resource-scarce target domain, and exploit that invariant to transfer knowledge fromsource domain to target domain. Based on approaches used to conduct transfer learning, Pan andYang [2010] divides transfer learning into mainly three categories: (i) instance-based transfer,(ii) feature-based transfer, and (iii) model-based transfer. FTL extends the traditional transferlearning to the privacy-preserving distributed machine learning (DML) paradigm. Here, wedescribe how these three categories of transfer learning techniques can be applied to HFL andVFL, respectively.

• Instance-based FTL. For HFL, data of participating parties are typically drawn fromdifferent distributions, which may lead to the poor performance of ML models trained onthose data. Participating parties can selectively pick or re-weight training data samples torelieve the distribution difference such that the objective loss function can be optimallyminimized. For VFL, participating parties may have quite different business objectives.Thus, aligned samples and some of their features may have a negative impact on the fed-erated transfer learning, which is referred to as negative transfer [Pan and Yang, 2010]. Inthis scenario, participating parties can selectively choose features and samples for avoidingnegative transfer.

• Feature-based FTL. Participating parties collaboratively learn a common feature repre-sentation space, in which the distribution and semantic difference among feature repre-sentations transformed from raw data can be relieved and such that knowledge can betransferable across different domains. For HFL, the common feature representation spacecan be learned through minimizing the maximum mean discrepancy (MMD) [Pan et al.,2009] among samples of participating parties. While for VFL, the common feature repre-sentation space can be learned through minimizing the distance between representationsof aligned samples belonging to different parties.

• Model-based FTL. Participating parties collaboratively learn shared models that can ben-efit for transfer learning. Alternatively, participating parties utilize pre-trained models asthe whole or part of the initial models for a federated learning task. HFL is a kind ofmodel-based FTL since during training a shared global model is being learned based on

data of all parties, and that shared global model is served as a pre-trained model to be fine-tuned by each party in each communication round [McMahan et al., 2016a]. For VFL,predictive models can be learned from aligned samples for inferring missing features andlabels (i.e., the blank spaces in Figure 1.4). Then, the enlarged training samples can be usedto train a more accurate shared model.

Formally, FTL aims to provide solutions for situations when:

$$
\mathcal {X} _ {i} \neq \mathcal {X} _ {j}, \mathcal {Y} _ {i} \neq \mathcal {Y} _ {j}, \mathcal {I} _ {i} \neq \mathcal {I} _ {j}, \forall \mathcal {D} _ {i}, \mathcal {D} _ {j}, i \neq j, \tag {6.1}
$$

where $\mathcal { X } _ { i }$ and $\mathcal { V } _ { i }$ denote the feature space and the label space of the ith party, respectively; $\mathscr { T } _ { i }$stands for the sample space, and matrix $\mathcal { D } _ { i }$ represents the dataset held by the ith party [Yanget al., 2019]. The objective is to predict labels for newly incoming samples or existing unlabeledsamples as accurately as possible.

In Section 6.3, we will introduce a secure feature-based FTL framework proposed by Liuet al. [2019] that helps predict labels for target domain by exploiting knowledge transferred fromsource domain.

From the technical perspective, FTL differs from traditional transfer learning mainly inthe following two ways.

• FTL builds models based on data distributed among multiple parties, and the data be-longing to each party cannot be gathered together or exposed to other parties. Traditionaltransfer learning has no such constraint.

• FTL requires the preservation of user privacy and the protection of data (and model)security, which is not a significant concern in traditional transfer learning.

FTL brings traditional transfer learning into the privacy-preserving DML paradigm.Therefore, we should define the security that a FTL system must guarantee.

Definition 6.1 Security definition of a FTL system. An FTL system typically involves twoparties, namely the source domain party and the target domain party. A multi-party FTL systemcan be regarded as a combination of multiple two-party FTL subsystems. It is assumed thatboth parties are honest-but-curious. That is, all parties in the federation follow the federationprotocols and rules but they will try to deduce information from data received. Consider a threatmodel with a semi-honest adversary who can corrupt at most one of the two parties of a two-party FTL system. For a protocol $P$ performing $( O _ { A } , O _ { B } ) = P ( I _ { A } , I _ { B } )$ , where $O _ { A }$ and $O _ { B }$are party A’s and party B’s respective outputs, and $I _ { A }$ and $I _ { B }$ are their respective inputs, $P$ issecure against party A if there exists an infinite number of $( I _ { B } ^ { \prime } , O _ { B } ^ { \prime } )$ pairs such that $( O _ { A } , O _ { B } ^ { \prime } ) =$$P ( I _ { A } , I _ { B } ^ { \prime } )$ . Such a security definition has been adopted in Du et al. [2004]. It provides a practicalsolution to control information disclosure as compared to complete zero knowledge security.

# 6.3 THE FTL FRAMEWORK

In this section, we introduce a secure feature-based FTL framework proposed by Liu et al.[2019]. Figure 6.1 illustrates this FTL framework in which a predictive model learned fromfeature representations of aligned samples belonging to party A and party B is utilized to predictlabels for unlabeled samples of party B.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/094b5ac65905e7ad81c439501c903f1d77c9f570a56555beacee84b56c558f50.jpg)



Figure 6.1: Illustration of FTL [Yang et al., 2019]. A predictive model learned from featurerepresentations of aligned samples belonging to party A and party B is utilized to predict labelsfor unlabeled samples of party B.


Consider a source domain party A with dataset $\mathcal { D } _ { A } : = \{ ( x _ { i } ^ { A } , y _ { i } ^ { A } ) \} _ { i = 1 } ^ { N _ { A } }$ where $x _ { i } ^ { A } \in R ^ { a }$ and$y _ { i } ^ { A } \in \{ + 1 , - 1 \}$ is the ith label, a target domain party B with dataset $\mathcal { D } _ { B } : = \{ x _ { j } ^ { B } \} _ { j = 1 } ^ { N _ { B } }$ fx Bj gNBj D1 where$x _ { j } ^ { B } \in R ^ { a } . { \mathcal { D } } _ { A } , { \mathcal { D } } _ { B }$ are separately held by two private parties and cannot be exposed to each other.We also assume that there exists a limited seta small set of labels for B’s data in party A: $\mathcal { D } _ { A B } : = \{ ( x _ { i } ^ { A } , x _ { i } ^ { B } ) \} _ { i = 1 } ^ { N _ { A B } }$ ander of$\mathcal { D } _ { c } : = \{ ( x _ { i } ^ { B } , \bar { y } _ { i } ^ { A } ) \} _ { i = 1 } ^ { \tilde { N _ { c } } }$ $N _ { c }$available target labels.

Without loss of generality, we assume all labels are in party A, but all the description herecan be adapted to the case where labels exist in party B. One can find the commonly sharedsample ID set in a privacy-preserving setting by masking data IDs with encryption techniquessuch as the RSA scheme. Here, we assume that A and B already found or both know theircommonly shared sample IDs. Given the above setting, the objective is for the two parities tocollaboratively build a transfer learning model to predict labels for the target-domain party B asaccurately as possible without exposing data to each other.

In recent years, DNNs have been widely adopted in transfer learning to find the im-plicit transfer mechanism [Oquab et al., 2014]. Here, we explore a general scenario in which

hidden representations of A and B are produced by two neural networks $u _ { i } ^ { A } = N e t ^ { A } ( x _ { i } ^ { A } )$ and$u _ { i } ^ { B } = N e t ^ { \bar { B } } ( x _ { i } ^ { B } )$ , where $u ^ { A } \in \mathbb { R } ^ { N _ { A } \times d }$ and $\mathbf { \bar { \Phi } } _ { u } ^ { B } \in \mathbb { R } ^ { N _ { B } \times d }$ , $d$ is the dimension of the hidden repre-sentation layer. Figure 6.2 illustrates the architecture of two neural networks.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/4afa373f96e135a058cd9cf003e4b6bc1210b51b336fda0e45b4a965eb1bfe67.jpg)



Figure 6.2: The architecture of neural networks of source and target domains.


To label the data in the target domain, a general approach is to introduce a predictionfunction $\varphi ( u _ { j } ^ { B } ) = \varphi ( u _ { 1 } ^ { A } , y _ { 1 } ^ { A } \ldots u _ { N _ { A } } ^ { A ^ { - } } , y _ { N _ { A } } ^ { A } , u _ { j } ^ { B } )$ . For example, Shu et al. [2015] used a translatorfunction, $\begin{array} { r } { \varphi ( u _ { j } ^ { B } ) = \frac { 1 } { N _ { A } } \sum _ { i } ^ { N _ { A } } y _ { i } ^ { A } u _ { i } ^ { A } ( u _ { j } ^ { B } ) ^ { \prime } . } \end{array}$ N i We can then write the training objective function usingthe available labeled dataset as:

$$
\min  _ {\Theta^ {A}, \Theta^ {B}} \mathcal {L} _ {1} = \sum_ {i} ^ {N _ {c}} \ell_ {1} \left(y _ {i} ^ {A}, \varphi \left(u _ {i} ^ {B}\right)\right), \tag {6.2}
$$

where numbe $\Theta ^ { A }$ , f $\Theta ^ { B }$ are trs for g paand ters of Net  and Net, respectively. Then, , $L _ { A }$ $L _ { B }$ be the where$N e t ^ { A }$ $N e t ^ { B }$ $\Theta ^ { A } = \{ \theta _ { l } ^ { A } \} _ { l = 1 } ^ { L _ { A } }$ ‚B $\Theta ^ { B } = \{ \theta _ { l } ^ { B } \} _ { l = 1 } ^ { L _ { B } }$$\theta _ { l } ^ { A }$ and $\theta _ { l } ^ { B }$ are the training parameters for the lth layer. $\ell _ { 1 }$ D   Ddenotes the loss function. For logisticloss, $\ell _ { 1 } ( y , \varphi ) = \log ( 1 + e ^ { - y \varphi } )$ .

In addition, we also aim to minimize the alignment loss between A and B.

$$
\min  _ {\Theta^ {A}, \Theta^ {B}} \mathcal {L} _ {2} = - \sum_ {i} ^ {N _ {A B}} \ell_ {2} \left(u _ {i} ^ {A}, u _ {i} ^ {B}\right), \tag {6.3}
$$

where $\ell _ { 2 }$ denotes the alignment loss which can be represented as $- u _ { i } ^ { A } ( u _ { i } ^ { B } ) ^ { \prime }$ or $| | u _ { i } ^ { A } - u _ { i } ^ { B } | | _ { F } ^ { 2 }$ .For simplicity, we assume it can be expressed in the form $\ell _ { 2 } ( u _ { i } ^ { A } , u _ { i } ^ { B } ) = \ell _ { 2 } ^ { A } ( u _ { i } ^ { A } ) + \ell _ { 2 } ^ { B } ( u _ { i } ^ { B } ) +$$\kappa u _ { i } ^ { A } ( u _ { i } ^ { B } ) ^ { \prime }$ , where $\kappa$ is a constant.

The final objective function is:

$$
\min  _ {\theta^ {A}, \theta^ {B}} \mathcal {L} = \mathcal {L} _ {1} + \gamma \mathcal {L} _ {2} + \frac {\lambda}{2} \left(\mathcal {L} _ {3} ^ {A} + \mathcal {L} _ {3} ^ {B}\right), \tag {6.4}
$$

where $\gamma$ and $\lambda$ are the weight parameters, and $\begin{array} { r } { \mathcal { L } _ { 3 } ^ { A } = \sum _ { l } ^ { L _ { A } } | | \theta _ { l } ^ { A } | | _ { F } ^ { 2 } , \mathcal { L } _ { 3 } ^ { B } = \sum _ { l } ^ { L _ { B } } | | \theta _ { l } ^ { B } | | _ { F } ^ { 2 } } \end{array}$ are theregularization terms.

The next step is to obtain the gradients for updating $\Theta ^ { A }$ , $\Theta ^ { B }$ through back propagation.For $i \in \{ A , B \}$ , we have

$$
\frac {\partial \mathcal {L}}{\partial \theta_ {l} ^ {i}} = \frac {\partial \mathcal {L} _ {1}}{\partial \theta_ {l} ^ {i}} + \gamma \frac {\partial \mathcal {L} _ {2}}{\partial \theta_ {l} ^ {i}} + \lambda \theta_ {l} ^ {i}. \tag {6.5}
$$

Under the condition that A and B shall not expose their raw data, privacy-preserving approachesneed to be developed to compute the loss in Equation (6.4) and the gradients in Equation (6.5).We describe two secure federated transfer learning approaches at high level for computing Equa-tions (6.4) and (6.5). One is based on homomorphic encryption [Acar et al., 2018] and the otheris based on secret sharing. In both approaches, we adopt second-order Taylor approximation forcomputing (6.4) and (6.5).

# 6.3.1 ADDITIVELY HOMOMORPHIC ENCRYPTION

Additively homomorphic encryption [Acar et al., 2018] and polynomial approximations havebeen widely used for privacy-preserving ML. The trade-offs between efficiency and privacy byadopting such approximations have been discussed in detail in Aono et al. [2016], Kim et al.[2018], and Phong et al. [2018]. Applying Equations (6.4) and (6.5), and additively homomor-phic encryption (denoted as ŒŒ, see also Section 2.4.2), we obtain the privacy preserved lossfunction and the corresponding gradients for the two domains as:

$$
[ [ \mathcal {L} ] ] = [ [ \mathcal {L} _ {1} ] ] + [ [ \gamma \mathcal {L} _ {2} ] ] + \left[ \left[ \frac {\lambda}{2} \left(\mathcal {L} _ {3} ^ {A} + \mathcal {L} _ {3} ^ {B}\right) \right] \right], \tag {6.6}
$$

$$
\left[ \left[ \frac {\partial \mathcal {L}}{\partial \theta_ {l} ^ {B}} \right] \right] = \left[ \left[ \frac {\partial \mathcal {L} _ {1}}{\partial \theta_ {l} ^ {B}} \right] \right] + \left[ \left[ \gamma \frac {\partial \mathcal {L} _ {2}}{\partial \theta_ {l} ^ {B}} \right] \right] + \left[ \left[ \lambda \theta_ {l} ^ {B} \right] \right] \tag {6.7}
$$

$$
\left[ \left[ \frac {\partial \mathcal {L}}{\partial \theta_ {l} ^ {A}} \right] \right] = \left[ \left[ \frac {\partial \mathcal {L} _ {1}}{\partial \theta_ {l} ^ {A}} \right] \right] + \left[ \left[ \gamma \frac {\partial \mathcal {L} _ {2}}{\partial \theta_ {l} ^ {A}} \right] \right] + \left[ \left[ \lambda \theta_ {l} ^ {A} \right] \right]. \tag {6.8}
$$

Let $[ [ \cdot ] ] _ { A }$ and $[ [ \cdot ] ] _ { B }$ be homomorphic encryption operators with public keys from A andB, respectively. Let $[ [ ( \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } } ) ^ { A } ] ] _ { A }$ be a set of intermediate components computed and encrypted

by party A for calculating $[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } } ] ]$ . Let $[ [ ( \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } ) ^ { B } ] ] _ { B } , [ [ \mathcal { L } ^ { B } ] ] _ { B }$ be a set of intermediate componentscomputed and encrypted by party B for calculating $[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } ] ]$ , $[ [ \mathcal { L } ] ]$ , respectively.

Note that we exclude mathematical details of loss and gradients calculation, and focus onthe collaboration between participating parties. We refer interested readers to Liu et al. [2019]for detailed explaination of the secure FTL framework.

# 6.3.2 THE FTL TRAINING PROCESS

With Equations (6.6), (6.7), and (6.8), we can now design a federated algorithm for trainingthe FTL model. The training process contains the following steps.

• Step 1: Party A and party B initialize and run their independent neural networks NetA andNetB locally to obtain hidden representations $u _ { i } ^ { A }$ and $u _ { i } ^ { \hat { B } }$ .

• Step 2: Party A computes and encrypts a list of intermediate components, denoted as$[ [ ( \frac { \bar { \partial } \mathcal { L } } { \partial \theta _ { l } ^ { B } } ) ^ { A } ] ] _ { A }$ and sends them to B to assist with the calculations of gradients L@ B $\frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } }$ . Whileparty B computes and encrypts a list of intermediate components, denoted as $[ [ ( \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } ) ^ { B } ] ] _ { B }$ /B B ,$[ [ \mathcal { L } ^ { B } ] ] _ { B }$ , and sends them to A to assist with the calculations of gradients $\frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } }$ and loss $\mathcal { L }$ .

• Step 3: Based on $[ [ ( \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } ) ^ { B } ] ] _ { B }$ and $[ [ { \mathcal { L } } ^ { B } ] ] _ { B }$ received, party A computes $[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } ] ] _ { B }$ and $[ [ { \mathcal { L } } ] ] _ { B }$via (6.6) and (6.8). Then party A creates random mask $m ^ { A }$ and add it to ŒŒ @L@A B to obtain $[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } ] ] _ { B }$$[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } + m ^ { A } ] ] _ { B }$ . Party A sends $[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } + m ^ { A } ] ] _ { B }$ and $[ [ { \mathcal { L } } ] ] _ { B }$ to B. Based on $\bigl [ \bigl [ \bigl ( \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } } \bigr ) ^ { A } \bigr ] \bigr ] _ { A }$ re-ceived, party B computes $[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } } ] ] _ { A }$ via Equation (6.7). Then party B creates random mask$m ^ { B }$ and add it to $[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } } ] ] _ { A }$ to obtain $[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } } + m ^ { B } ] ] _ { A }$ . Party B sends $[ [ \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } } + m ^ { B } ] ] _ { A }$ to A.

• Step 4: Party A decrypts $\frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } } + m ^ { B }$ and sends it to B. While party B decrypts $\frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } + m ^ { A }$and $\mathcal { L }$ , and sends them to A.

• Step 5: Party A and party B remove random masks and obtain gradients $\frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } }$ and $\frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } }$respectively. Then the two parties update their respective model with the decrypted gradi-ents.

• Step 6: Party A sends termination signals to B once the loss $\mathcal { L }$ converges . Otherwise, goesto step 1 to continue the training process.

Recently, there are a large number of works discussing the potential risks associated withindirect privacy leakage through gradients [Bonawitz et al., 2016, Hitaj et al., 2017, McSherry,2017, Phong et al., 2018, Shokri and Shmatikov, 2015]. To prevent the two parties from know-ing each other’s gradients, A and B further mask their own gradient with an encrypted random

value. A and B then exchange the encrypted masked gradients and loss and obtain the decryptedvalues. Here, the encryption step is to prevent a malicious third-party from eavesdropping thetransmissions, while the masking step is to prevent A and B from knowing each other’s exactgradient value.

# 6.3.3 THE FTL PREDICTION PROCESS

Once the FTL model has been trained, it can be used to provide predictions for unlabeled datain party B. The prediction process for each unlabeled data point involves the following steps.

• Step 1: Party B computes $u _ { j } ^ { B }$ with the trained neural network parameters $\Theta ^ { B }$ , and sendsencrypted $[ [ u _ { j } ^ { B } ] ]$ to party A.

• Step 2: Party A evaluates $u _ { j } ^ { B }$ and masks the result with a random value, and sends theencrypted and masked $[ [ \varphi ( u _ { j } ^ { B } ) + m ^ { A } ] ] _ { B }$ to B.

• Step 3: Party B decrypts $[ [ \varphi ( u _ { j } ^ { B } ) + m ^ { A } ] ] _ { B }$ and sends $\varphi ( u _ { j } ^ { B } ) + m ^ { A }$ back to party A.

• Step 4: Party A obtains $\varphi ( u _ { j } ^ { B } )$ and the label $y _ { j } ^ { B }$ , and sends the label $y _ { j } ^ { B }$ to B.

Note that the only source of performance loss over the secure FTL process is second-order Taylor approximation of the final loss function, rather than at every nonlinear activationlayer of the neural network [Hesamifard et al., 2017]. The computations inside the networks areunaffected. As demonstrated in Liu et al. [2019], the errors in loss and gradient calculations, aswell as the loss in accuracy by adopting our approach are minimal. Therefore, the approach isscalable and flexible to changes in neural network structures.

# 6.3.4 SECURITY ANALYSIS

As demonstrated in Liu et al. [2019], both the FTL training process and the FTL predictionprocess are secure under our security definition (see Definition 6.1), provided that the underlyingadditively homomorphic encryption scheme is secure.

During training, raw data $\mathcal { D } _ { A }$ and $\mathcal { D } _ { B }$ , as well as the local models NetA and NetB are neverexposed and only the encrypted hidden representations are exchanged. In each iteration, the onlynon-encrypted values party A and party B receive are the gradients of the model parameters,which are aggregated from all variables and masked by random numbers. At the end of thetraining process, each party (A or B) remains oblivious to the data structure of the other partyand each obtains model parameters associated only with its own features. At inference time, thetwo parties need to collaborate in order to compute the prediction results.

Note the protocol does not deal with a malicious party. If party A fakes its inputs andsubmits only one non-zero input, it may be able tell the value of $u _ { i } ^ { B }$ at the position of that input.It still cannot tell $x _ { i } ^ { B }$ or $\Theta _ { B }$ , and neither party will be able to obtain correct results.

# 6.3.5 SECRET SHARING-BASED FTL

Homomorphic encryption techniques are capable of providing a high level of security for the in-formation or knowledge shared among parties, thereby protecting the privacy of data and modelsbelonging to each party. However, homomorphic encryption techniques typically need exten-sive computational resources and massive parallelization to scale, which make them impracticalin many applications that require real-time throughput.

An alternative secure protocol to homomorphic encryption is secret sharing. The biggestadvantages of the secret sharing approach include (i) there is no accuracy loss, and (ii) com-putation is much more efficient than homomorphic encryption approach. The drawback of thesecret sharing approach is that one has to offline generate and store many triplets before onlinecomputation.

To facilitate the description of secret sharing-based FTL algorithm, we rewrite Equa-tions (6.6), (6.7), and (6.8) as follows:

$$
\mathcal {L} = \mathcal {L} _ {\mathcal {A}} + \mathcal {L} _ {\mathcal {B}} + \mathcal {L} _ {\mathcal {A B}} \tag {6.9}
$$

$$
\frac {\partial \mathcal {L}}{\partial \theta_ {\ell} ^ {B}} = \left(\frac {\partial \mathcal {L}}{\partial \theta_ {\ell} ^ {B}}\right) _ {B} + \left(\frac {\partial \mathcal {L}}{\partial \theta_ {\ell} ^ {B}}\right) _ {A B} \tag {6.10}
$$

$$
\frac {\partial \mathcal {L}}{\partial \theta_ {l} ^ {A}} = \left(\frac {\partial \mathcal {L}}{\partial \theta_ {l} ^ {A}}\right) _ {A} + \left(\frac {\partial \mathcal {L}}{\partial \theta_ {l} ^ {A}}\right) _ {A B}, \tag {6.11}
$$

where $\mathcal { L } _ { A }$ and $\big ( \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } \big ) _ { A }$ are computed solely by party A, and $\mathcal { L } _ { B }$ and $\big ( \frac { \partial \mathcal { L } } { \partial \theta _ { \ell } ^ { B } } \big ) _ { B }$ @ are computed solelyby party B. $\mathcal { L } _ { A B }$ , $\big ( \frac { \partial \mathcal { L } } { \partial \theta _ { \ell } ^ { B } } \big ) _ { A B }$ and $\big ( \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } \big ) _ { A B }$ are computed collaboratively by A and B through secretsharing scheme.

The whole process of computing (6.9), (6.10), and (6.11) can be performed securelythrough secret sharing with the help of Beaver’s triples. The secret sharing-based FTL train-ing process is summarized in the following steps.

• Step 1: Party A and party B initialize and run their independent neural networks NetA andNetB locally to obtain hidden representations $u _ { i } ^ { A }$ and $u _ { i } ^ { \bar { B } }$ .

• Step 2: Party A and party B collaboratively computes $\mathcal { L } _ { A B }$ through secret sharing. Party Acomputes $\mathcal { L } _ { A }$ and sends it to party B. Party B computes $\mathcal { L } _ { B }$ and sends it to party A.

• Step 3: Party A and party B individually reconstruct loss $\mathcal { L }$ via Equation (6.9).

• Step 4: Party A and party B collaboratively computes $( \frac { \partial \mathcal { L } } { \partial \theta _ { \ell } ^ { A } } ) _ { A B }$ and $\big ( \frac { \partial \mathcal { L } } { \partial \theta _ { \ell } ^ { B } } \big ) _ { A B }$ through secretsharing.

• Step 5: Party A computes its gradients via $\begin{array} { r } { \frac { \partial \mathcal { L } } { \partial \theta _ { \ell } ^ { A } } = ( \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { A } } ) _ { A } + ( \frac { \partial \mathcal { L } } { \partial \theta _ { \ell } ^ { A } } ) _ { A B } } \end{array}$ . @L@Al /A C . @L@A` /AB and updates its localmodel $\theta _ { \ell } ^ { A }$ . While at the same time, party B computes its gradients via $\begin{array} { r } { \frac { \partial \mathcal { L } } { \partial \theta _ { \ell } ^ { B } } = ( \frac { \partial \mathcal { L } } { \partial \theta _ { l } ^ { B } } ) _ { B } \ + } \end{array}$ . @L@ B /B C$\big ( \frac { \partial \mathcal { L } } { \partial \theta _ { \ell } ^ { B } } \big ) _ { A B }$ and updates it local model $\theta _ { \ell } ^ { B }$ ;

• Step 6: Party A sends termination signals to B once the loss $\mathcal { L }$ converges. Otherwise, goesto step 1 to continue the training process.

After training is completed, we proceed to the prediction phase. At the high level, the predictionprocess is quite simple. It involves the following two steps.

• Step 1: Party A and party B run their trained neural networks $N e t ^ { A }$ and NetB locally toobtain hidden representations $u _ { i } ^ { A }$ and $u _ { i } ^ { B }$ .

• Step 2: based on $u _ { i } ^ { A }$ and $u _ { i } ^ { B }$ , party A and party B collaboratively reconstruct $\varphi ( u _ { j } ^ { B } )$ throughsecret sharing and calculate the label $y _ { j } ^ { B }$ .

Note that in both training and prediction processes, the only information that any party receivesregarding any private value of the other party is only a share of that private value based on thesecret sharing scheme. Therefore, no party is able to learn any information about the privatevalues it is not supposed to learn.

# 6.4 CHALLENGES AND OUTLOOK

Traditional transfer learning is typically conducted in sequential or centralized way. Sequentialtransfer learning [Ruder, 2019] means that transfer knowledge is first learned on source taskand then applied to target domain to improve the performance of the target model. Sequentialtransfer learning is ubiquitous and effective in computer vision where it is typically practicedin the form of pretrained model on large image datasets such as ImageNet [Bagdasaryan etal., 2009]. It is also commonly used in natural language processing to encode language units(e.g., word, sentence or document) in the form of distributed representations. The centralizedtransfer learning indicates that the models and data involved in transfer learning are locatedin one place. Thus, traditional transfer learning is not applicable in many practical applicationswhere data is scattered among multiple parties and its privacy is a major concern. FTL is afeasible and promising solution to address those issues.

Research work on incorporating transfer learning into federated learning framework isfast-growing. However, for practical applications, FTL still faces many challenges. We list threeof them as follows.

• We need to develop schemes to learn the transferable knowledge in a way that it canwell capture the invariant between participants. Different from sequential and centralizedtransfer learning where the transfer knowledge is typically represented in one universal

pre-trained model, transfer knowledge in FTL is distributed among local models. Eachparticipant has total control in designing and training its local model. A balance shouldbe achieved between autonomy and generalization performance of the FTL models.

• We need to determine how to learn a representation of transfer knowledge in a distributedenvironment while preserving the privacy of the shared representation of all participants.Under the federated learning framework, transfer knowledge is not only learned in a dis-tributed manner, but also is typically not allowed to be exposed to any participant. Thus, weneed to figure out precisely what each participant contributes to the shared representationin the federation and consider how to preserve the privacy of the shared representation.

• We need to design efficient secure protocols that can be employed in federated transferlearning. FTL usually requires closer interactions among participants in terms of com-munication frequency and the size of transferred data. Careful consideration should betaken when designing or choosing secure protocols in order to achieve a balance betweensecurity and overhead.

There are certainly many other challenges that are waiting for researchers and engineersto address. We envision that with the high practical value brought by FTL, more and more in-stitutes and enterprises would invest resources and efforts into the research and implementationof FTL.

# Incentive Mechanism Designfor Federated Learning

In federated learning, motivating data owners to continue participating in a data federation isan important challenge. The key to achieving this objective is to device an incentive scheme thatshares the profit generated by a federation with participants in a fair and just manner. Before thisstep can be achieved, a mechanism for evaluating the contribution toward the federated modelby a given data owner must be established. Although there has yet to be published researchon solving this problem, there has been a well-established line of work on using auction-basedapproaches to motivate sensors to commit more resources to improve data quality, which mightshed light into solving this problem.

In this chapter, we provide an overview of the problem of evaluating data owners’ con-tributions and highlight some reverse auction-based approaches which are promising to be fur-ther developed to help address the problem of evaluating data owner contributions in federatedlearning. Following this discussion, we introduce a framework for fairness-aware profit sharingbased on such evaluation results—the Federated Learning Incentivizer (FLI) payoff-sharingscheme [Yu et al., 2020]. It provides a blueprint for further advances in eliciting high qualitycontributions from data owners to be applied in situations in which data owners need to receivedelayed payments for their rewards since the federation must use the federated model to generaterevenue first.

# 7.1 PAYING FOR CONTRIBUTIONS

For a federation, data owners’ continued participation in the federated learning process (e.g.,through sharing of encrypted model parameters) is key to its long-term success. The contribu-tions by data owners to a federation are used to build a machine learning (ML) model which, inturn, can be used to generate revenues. The federation can share part of the revenue with dataowners as incentives (Figure 7.1). The research question here is how to quantify the payoff foreach data owner in a context-aware manner in order to achieve long-term sustainable operation.

# 7.1.1 PROFIT-SHARING GAMES

Similar research problems have also been studied under the topic of cost-sharing games. Ingeneral, there are three categories of widely used profit-sharing schemes.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/8be15d640105b05ba86045275513f6f3fbd00aae0587c88ea16201eb3f06cb9e.jpg)



Figure 7.1: Transfer of utility from a data federation to its participants.


1. Egalitarian: any unit of utility produced by a data federation is divided equally among thedata owners who helped produce it.

2. Marginal gain: the payoff of a data owner in a data federation is the utility that the teamgained when she joined.

3. Marginal loss: the payoff of a data owner in a data federation is the utility that the teamwould lose if she were to leave.

In general, a participant i’s payoff from a total budget $B ( t )$ in a given round of profit-sharing t,denoted as ${ \hat { u } } _ { i } ( t )$ , is computed as:

$$
\hat {u} _ {i} (t) = \frac {u _ {i} (t)}{\sum_ {i = 1} ^ {N} u _ {i} (t)} B (t), \tag {7.1}
$$

where $u _ { i } ( t )$ is $i$ ’s share of $B ( t )$ among his peers computed following a given scheme.

Equal division is an example of egalitarian profit-sharing [Yang et al., 2017]. Under thisscheme, the available profit-sharing budget, $B ( t )$ , at a given round t is equally divided amongall $N$ participants. Thus, a participant $i$ ’s payoff is:

$$
u _ {i} (t) = \frac {1}{N}. \tag {7.2}
$$

Under the Individual profit-sharing scheme [Yang et al., 2017], each participant i’s owncontribution to the collective (assuming the collective only contains $i$ ), is used to determine hisshare of the profit, $u _ { i } ( t )$ :

$$
u _ {i} (t) = v (\{i \}), \tag {7.3}
$$

where $v ( X )$ is a function evaluating the utility of a collective $X$ .

The Labor Union game [Gollapudi et al., 2017] profit-sharing scheme determines i’sshare of $B ( t )$ based on his marginal contribution to the utility of the collective formed by his

predecessors $F$ (i.e., each participant’s marginal contribution is computed based on the samesequence as they joined the collective):

$$
u _ {i} (t) = v (F \cup \{i \}) - v (F). \tag {7.4}
$$

The Shapley game profit-sharing scheme [Augustine et al., 2015] is also a marginal contribution-based scheme. Unlike the Labor Union game, Shapley game aims to eliminate the effect of theparticipants joining the collective in different sequences in order to more fairly estimate theirmarginal contributions to the collective. Thus, it averages the marginal contribution for each iunder all different permutations of the $i$ joining the collective relative to other participants:

$$
u _ {i} (t) = \sum_ {P \subseteq P _ {j} \backslash \{i \}} \frac {| P | ! (| P _ {j} | - | P | - 1) !}{| P _ {j} |} [ v (P \cup \{i \}) - v (P) ], \tag {7.5}
$$

where a collective is divided into m parties $( P _ { 1 } , P _ { 2 } , \ldots , P _ { m } )$

The Fair-value game scheme [Gollapudi et al., 2017] is a marginal loss-based scheme.Under this scheme, i’s share of the profit is determined by:

$$
u _ {i} (t) = v (F) - v (F \setminus \{i \}). \tag {7.6}
$$

The sequence following which the participants leave a collective significantly affects his payoff.

# 7.1.2 REVERSE AUCTIONS

Other than profit-sharing game-based approaches, reverse auctions have also been used to de-velop incentive schemes that promote the quality of contributed data. There have been reverseauction schemes for sensor data [Singla and Krause, 2013], with the goal of finding the cheapestcombination of sensors that provide data with the quality level. Such approaches are based on theassumption that the central entity knows what data is needed (e.g., geographical distribution).However, these approaches typically assume the data quality is independent of cost (since re-verse auction requires identical items). They might also encourage arbitrage through submittinguninformative data just to collect rewards which is an unintended consequence.

Another way is to obtain data of a given quality is through posted rewards. This is a take-it-or-leave-it scheme. The federation could post a fixed reward to be paid for data owners who cancontribute data with a certain quality level. The data owners can choose to participate in federatedmodel training if their cost is lower than the reward; or not to participate if their cost is toohigher than the reward. When effort from a data owner is required in order to meet the qualityrequirement, there are three existing categories of schemes for designing the rewards [Faltingsand Radanovic, 2017]:

1. through output agreement [Dasgupta and Ghosh, 2013, Shnayder et al., 2016];

2. through information theoretic analysis [Kong and Schoenebeck, 2013]; and

3. through model improvement [Radanovic et al., 2016].

For gradient-based federated learning approaches, the gradient information can be re-garded as a type of data. However, in these cases, output agreement-based rewards are hard toapply as mutual information requires a multi-task setting which is usually not present in suchcases. Thus, among these three categories of schemes, model improvement is the most relevantway of designing rewards for federated learning. There are two emerging federated learning in-centive schemes focused on model improvement.

Richardson et al. [2019] proposed a scheme which pays for marginal improvementsbrought about by model updates. The sum of improvements might result in overestimation ofcontribution. Thus, the proposed approach also includes a model for correcting the overesti-mation issue. This scheme ensures that payment is proportional to model quality improvement,which means the budget for achieving a target model quality level is predictable. It also ensuresthat data owners who submit model updates early receive a higher reward. This motivates themto participate even in early stages of the federated model training process.

Jia et al. [2019] is similar to Richardson et al. [2019], but computes a Shapley value to splitreward among data owners. Such computations tend to be expensive. Instead, approximation byscaling factor adopted by Radanovic et al. [2016] can be much more computationally efficient.In addition, it does not address the issue that the same dataset can be contributed without extracost to multiple federations.

These two schemes guarantee that uninformative data do not receive reward so as to dis-courage free-riders.

# 7.2 A FAIRNESS-AWARE PROFIT SHARINGFRAMEWORK

The aforementioned schemes could be extended into situations in which the data owners are notpaid upfront, but rather, have to wait for the federated model to generate revenue before receiv-ing their rewards. In this section, we introduce a fairness-aware profit-sharing framework—FLI.It provides an architecture for incentive mechanism designers to consider such situations of de-layed payment and incorporated fairness into such cases to sustain long-term participation bydata owners.

# 7.2.1 MODELING CONTRIBUTION

The architecture of FLI is shown in Figure 7.2. We assume that the data federation followssynchronous mode of model training commonly adopted by federated learning [Bonawitz andEichner et al., 2019] in which data owners share their model parameters in rounds. In round $t$ ,a data owner i can contribute his local model trained on a dataset to a federation. The federationis able to assess the contribution of i’s data contribution to the federation following one of theprofit-sharing schemes discussed in the previous section as the FLI baseline scheme.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-21/02ed02bd-46d8-40f2-bfc0-a7f05b97108d/d4da4c597662f89feab2118b8de776e697af55fdd99ec12e1bd344a3b47a1362.jpg)



Figure 7.2: The overview of FLI.


To do so, a federation can run a sandbox simulation to estimate the effect of a data owner’scontribution on model performance. The assessment outcome is recorded by a variable $q _ { i } ( t ) \geqslant$0, which denotes the expected marginal revenue the federated model can gain with i’s latestcontribution. The proposed incentive scheme is fully decoupled from how such a contributionscore is produced. Thus, we do not focus on the exact mechanism by which $q _ { i } ( t )$ is produced,and assume the value is available to be used as an input for FLI.

# 7.2.2 MODELING COST

Let $c _ { i } ( t )$ be the cost for i to contribute $d _ { i } ( t )$ to the federation. There can be multiple ways tocompute $c _ { i } ( t )$ . Although it is possible to build computational models based on market research,a more practical solution is still auction-based self-report. A procurement auction [Mishra andVeeramani, 2007] can be used to estimate the cost when $c _ { i } ( t )$ is privately known. Specifically,the federation can ask each data owner to request a payment for the data contribution, and thenselect which data owner shall be allowed to join the federation.

In this case, the delayed payment scheme can be separated from the procurement auctionwhere $c _ { i } ( t )$ can be interpreted as the payment to data owner $i$ determined by the auction. Thisway, a clear separation of concern between the auction stage and the proposed incentive scheme

can be achieved. Here, since we focuses on developing the framework of incentive design forfederated learning, we leave the topic of computing $c _ { i } ( t )$ to be treated in another work, andassume that this value is available here.

# 7.2.3 MODELING REGRET

For each data owner $i$ , the federation keeps track of the payoff gained from contributing data tothe federation over time. As this value represents the difference between what the data ownerhas received so far and what he is supposed to receive, we refer to this term as regret, $Y _ { i } ( t )$ . Thedynamics of $Y _ { i } ( t )$ can be regarded as a queueing system:

$$
Y _ {i} (t + 1) \triangleq \max  \left[ Y _ {i} (t) + c _ {i} (t) - u _ {i} (t), 0 \right], \tag {7.7}
$$

where $u _ { i } ( t )$ is the payoff to be transferred to $i$ by the federation. A large value of $Y _ { i } ( t )$ indicatesthat $i$ has not been adequately compensated.

# 7.2.4 MODELING TEMPORAL REGRET

In some cases, the cost $c _ { i } ( t )$ may be too large to be fully covered by a single payment of $u _ { i } ( t )$ dueto budget limitation in the federation. In such cases, the federation needs to compute instalmentsto be paid out to the data owners in multiple rounds. Their share of the current payout budget,$B ( t )$ , depends on their regret as well as how long they have been waiting to receive the full payoff.

For this purpose, we complement Equation (7.7) with a temporal queue, $Q _ { i } ( t )$ , with queue-ing dynamics defined as:

$$
Q _ {i} (t + 1) \triangleq \max  \left[ Q _ {i} (t) + \lambda_ {i} (t) - u _ {i} (t), 0 \right], \tag {7.8}
$$

where $\lambda _ { i } ( t )$ is an indicator function:

$$
\lambda_ {i} (t) = \left\{ \begin{array}{l l} \hat {c} _ {i}, & \text {i f} Y _ {i} (t) > 0 \\ 0, & \text {o t h e r w i s e .} \end{array} \right. \tag {7.9}
$$

This formulation means that as long as $Y _ { i } ( t )$ is not empty, the temporal queue, $Q _ { i } ( t )$ , will in-crease. The increment is based on i’s average cost of data contribution to the federation, $\hat { c } _ { i }$ ,through past experience. Both queues decrease by the same amount when the federation paysi. The profit-sharing approach can ensure that data owners are compensated not only for theirdata contributions, but also for waiting to receive the full payoff, thereby making it “worth theirwhile” to attract them to the federation.

# 7.2.5 THE POLICY ORCHESTRATOR

In order to encourage data owners to continue participating in the federation, the federationneeds to ensure that the data owners are treated fairly based on their individual contribution.Here, we define three fairness criteria that are important to the long-term sustainable operationof a federation.

1. Contribution Fairness: a data owner i’s payoff shall be positively correlated to his contri-bution to the federation $q _ { i } ( t )$ .

2. Regret Distribution Fairness: the difference of the regret and the temporal regret amongdata owners shall be as small as possible.

3. Expectation Fairness: the fluctuation of data owners’ regret and temporal regret valuesover time shall be as small as possible.

In order to satisfy all the three fairness criteria, the federation shall maximize a “value-minus-regret drift” objective function over time. The collective utility derived from data owners’contributions is related to two factors: (1) the contribution to the federation by a data owner i$\left( q _ { i } ( t ) \right)$ and (2) the payoff that i receives from the federation for the contribution $\left( u _ { i } ( t ) \right)$ . It is fairthat a data owner who make significant contribution to the federation shall receive high payoff.Thus, we have:

$$
U = \frac {1}{T} \sum_ {t = 0} ^ {T - 1} \sum_ {i = 1} ^ {N} \left\{q _ {i} (t) u _ {i} (t) \right\}. \tag {7.10}
$$

Maximizing $U$ satisfies Fairness criterion (1).

Since $Y _ { i } ( 0 ) = 0$ for all $i$ , if we consistently strive to minimize the variation in $Y _ { i } ( t )$ overtime, the regret must not grow unbounded to drive data owners away. Based on recommenda-tions from the Belmont Report [1978], the federation needs to jointly consider the magnitudeand distribution of regret among data owners and over time in order to treat them fairly [Yuet al., 2018]. $l _ { 2 }$ -norm can capture simultaneously the magnitudes of the regret values and thedistribution of regret among data owners. A large $l _ { 2 }$ -norm value means there are many dataowners with none-zero regrets, and/or there are a few data owners with very large regret [Yu etal., 2015, 2016, 2019]. Both shall be minimized.

Based on the $l _ { 2 }$ -norm technique, we formulate the Lyapunov function [Neely, 2010] ofFLI as:

$$
L (t) = \frac {1}{2} \sum_ {i = 1} ^ {N} \left[ Y _ {i} ^ {2} (t) + Q _ {i} ^ {2} (t) \right]. \tag {7.11}
$$

For simplicity of derivation later, we omit the $\sqrt { \cdot }$ operator in the standard $l _ { 2 }$ -norm calculationand multiply the whole term with $\frac { 1 } { 2 }$ . These changes do not alter the desirable properties of$l _ { 2 }$ -norm for our formulation.

The drift in data owners’ regret over time is:

$$
\begin{array}{l} \Delta = \frac {1}{T} \sum_ {t = 0} ^ {T - 1} [ L (t + 1) - L (t) ] \\ = \frac {1}{T} \sum_ {t = 0} ^ {T - 1} \sum_ {i = 1} ^ {N} \left[ \frac {1}{2} Y _ {i} ^ {2} (t + 1) - \frac {1}{2} Y _ {i} ^ {2} (t) + \frac {1}{2} Q _ {i} ^ {2} (t + 1) - \frac {1}{2} Q _ {i} ^ {2} (t) \right] \tag {7.12} \\ \leqslant \frac {1}{T} \sum_ {t = 0} ^ {T - 1} \sum_ {i = 1} ^ {N} \left[ Y _ {i} (t) c _ {i} (t) - Y _ {i} (t) u _ {i} (t) + \frac {1}{2} c _ {i} ^ {2} (t) - c _ {i} (t) u _ {i} (t) + \frac {1}{2} u _ {i} ^ {2} (t) + Q _ {i} (t) \lambda_ {i} (t) \right. \\ \left. - Q _ {i} (t) u _ {i} (t) + \frac {1}{2} \lambda_ {i} ^ {2} (t) - \lambda_ {i} (t) u _ {i} (t) + \frac {1}{2} u _ {i} ^ {2} (t) \right]. \\ \end{array}
$$

Since $u _ { i } ( t )$ it the control variable here, we extract only terms containing it from Equation (7.13):

$$
\triangle \leqslant \frac {1}{T} \sum_ {t = 0} ^ {T - 1} \sum_ {i = 1} ^ {N} \left\{u _ {i} ^ {2} (t) - u _ {i} (t) \left[ Y _ {i} (t) + c _ {i} (t) + Q _ {i} (t) + \lambda_ {i} (t) \right] \right\}. \tag {7.13}
$$

The regret drift variable $\triangle$ jointly captures the distribution of regret (both $Y _ { i } ( t )$ and $Q _ { i } ( t ) )$ among data owners, as well as the fluctuation of regret over time. Minimizing $\triangle$ satisfies Fair-ness criteria (2) and (3).

By jointly considering collective utility and the distribution of regret, the overall objectivefunction for a given federation can be defined as “maximizing collective utility while minimizinginequality among data owners’ regret and waiting time”:

$$
\omega U - \triangle \tag {7.14}
$$

which shall be maximized. Here, $\omega$ is a regularization term for a federation to control the trade-off between the two objectives. Thus, the objective function of a federation is:

Maximize:

$$
\frac {1}{T} \sum_ {t = 0} ^ {T - 1} \sum_ {i = 1} ^ {N} \left\{u _ {i} (t) \left[ \omega q _ {i} (t) + Y _ {i} (t) + c _ {i} (t) + Q _ {i} (t) + \lambda_ {i} (t) \right] - u _ {i} ^ {2} (t) \right\} \tag {7.15}
$$

Subject to:

$$
\sum_ {i = 1} ^ {N} \hat {u} _ {i} (t) \leqslant B (t), \forall t \tag {7.16}
$$

$$
\hat {u} _ {i} (t) \geqslant 0, \forall i, t, \tag {7.17}
$$

where $\hat { u } _ { i } ( t ) \leqslant u _ { i } ( t )$ denotes the actual instalment payout from the federation to a data owner iin round $t$ , which will be derived in the following section.

# 7.2.6 COMPUTING PAYOFF WEIGHTAGE

In order to optimize Equation (7.15), we set its first derivative to 0 and solve for $u _ { i } ( t )$ :

$$
\frac {d}{d u _ {i} (t)} [ \omega U - \triangle ] = 0. \tag {7.18}
$$

Solving the above equation yields:

$$
u _ {i} (t) = \frac {1}{2} \left[ \omega q _ {i} (t) + Y _ {i} (t) + c _ {i} (t) + Q _ {i} (t) + \lambda_ {i} (t) \right]. \tag {7.19}
$$

The second derivative of Equation (7.15) is:

$$
\frac {d ^ {2}}{d u _ {i} ^ {2} (t)} [ \omega U - \triangle ] = - 1 <   0 \tag {7.20}
$$

indicating that the solution maximizes the objective function.

For contributing $d _ { i } ( t )$ amount of data of quality $q _ { i } ( t )$ at round $t$ , the data owner $i$ shallreceive a total compensation of $\begin{array} { r } { u _ { i } ( t ) = \frac { 1 } { 2 } [ \omega q _ { i } ( t ) + Y _ { i } ( t ) + c _ { i } ( t ) + Q _ { i } ( t ) + \lambda _ { i } ( t ) ] } \end{array}$ . The federa-tion may need to pay out this in instalments over a period of time if not enough budget, $B ( t )$ , isavailable to pay all data owners fully at round $t$ . To share $B ( t )$ among the data owners, the com-puted $u _ { i } ( t )$ values are used as weights to divide the budget $B ( t )$ . The actual payout instalmentto $i$ at t , ${ \hat { u } } _ { i } ( t )$ , is:

$$
\hat {u} _ {i} (t) = \frac {u _ {i} (t)}{\sum_ {i = 1} ^ {N} u _ {i} (t)} B (t). \tag {7.21}
$$

The FLI payoff-sharing scheme is summarized in Algorithm 7.1. It accounts for boththe magnitude and the temporal aspects of participating in a federation. Data owners who hascontributed a large set of high quality data, and who has not been fully compensated for a longtime will enjoy a higher share of subsequent revenues generated by the federation.

The computational time complexity of Algorithm 7.1 is $O ( N )$ . Once $Y _ { i } ( t )$ and $Q _ { i } ( t )$ bothreach 0 with no new cost incurred by i, $u _ { i } ( t ) = \omega q _ { i } ( t )$ . From then on, $i$ will share future payoffsbased on his contribution to the federation assessed using one of the baseline methods (e.g., theShapley game payoff-sharing scheme). The proposed scheme prioritizes compensating the dataowners with non-zero regret while taking into account their contributions to the federation.

# 7.3 DISCUSSIONS

In this chapter, we reviewed existing literature on profit-sharing games and reverse auctionswhich can be used to develop incentive mechanisms for federated learning, and highlightedsome recent developments that leveraged some aspects of these related works to encourage earlysubmission of high-quality contributions to the federation. Following this, we further proposed


Algorithm 7.1 Federated Learning Incentivizer (FLI)


Input:  $\omega$  and  $B(t)$  set by the system administrator;  $Y_{i}(t)$  from all data owners at round  $t$  (with  $Y_{i}(t) = 0$  for any  $i$  who just joined the federation); and  $Q_{i}(t)$  from all data owners at round  $t$  (with  $Q_{i}(t) = 0$  for any  $i$  who just joined the federation).  
1: Initialize  $S(t) \gets 0$ ; //to hold the sum of all  $u_{i}(t)$  values.  
2: for  $i = 1$  to  $N$  do  
3: if  $d_{i}(t) > 0$  then  
4: Compute  $c_{i}(t)$ ;  
5: Compute  $q_{i}(t)$ ;  
6: else  
7:  $c_{i}(t) = 0$ ;  
8: end if  
9:  $u_{i}(t) \gets \frac{1}{2} [\omega q_{i}(t) + Y_{i}(t) + c_{i}(t) + 