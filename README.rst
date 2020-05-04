NEO4J PROV-db connector / CSV converter. Application to the detection of epidemiological patterns of COVID19 and the implementation of a PROVn model for the monitoring of infections, proactive detection of vulnerabilities, management of confinement and clinical evolution of cases to assist in the progressive and selective reduction of quarantine.
https://medium.com/@grillotebis/author-7cf794d895a4

Author: Phd Candidate, Guillermo Gabriel Fernández Amado. Sys Engineer & Sociologist (Arg), History Phd std. (Spa), Certified neo4j developer, Developer of Banc Sabadell AML (Cat).
A pandemic proliferates through a network of connections. Fighting against a spreading pandemic is a massive, comprehensive issue that affects health, services supply chain and assistance social systems, as well as many other economic structures.
Graphs are perfectly suited for handling connected data, from tracing connections through complex networks to understanding dependencies between entities.
Tracing connections between people when they spend time together is a key aspect of how graphs are useful for responding to the spread of COVID-19, as well as identifying clusters of activity.
Another aspect is drug research and repurposing. By understanding how existing compounds work, which genes they affect and how genes are connected and related to each other, we open up opportunities to identify and reuse existing drugs.
At this moment a solution that Provenance (W3C) uses to manage epidemiological emergencies is lacking.
We are going to be able to create a COVID19 PROVn model, to be geo-referenced, base of each person case infected, record their evolution and time history using the PROV framework, and manage the information revenue using python and visualizing by Linkurious.
In this model, the Agents are people (infected, vulnerable and potentially infected, with symptoms, etc.).
Activities are previous actions that person did, as a retrospective of what he did in the last days (air travel, train, work, visits to people, meetings, assistance, health facilities, food, etc.) Entities will be potentially dangerous elements of infection (plane, train, facility, office, hospital, residence, apartment, route, building, supermarket, meeting, school, company, etc.).
Only in this way, we will be able to know in a retrospective way, the previous steps, recolected by surveys (done by the police, doctors, government, calls, etc.) of the affected agents and thus, for example, anticipate quarantine, and confine of agents, activities and / or entities, proceeding to inform the competent authorities of each case.
It provides a triple level of analysis, starting with a layer of contagion prevention and emergency action detecting communities and places of epidemiological risk. A second layer that provides information and analysis for a correct and efficient management of the orders of confinement, evolution and monitoring of each case. Finally a third layer that would be used as a knowledge base for medical and genetic research.
This model has three layers, one for incident management using activities like (incident, confine), a second for monitoring (evaluation, tracing) and the medical and genetics layer (to be expanded). The model is instantiated by a python program covid19_example.py, and use provconvert application to read a CSV file and make a use case from each row and load the csv to neo4j using PROVn notation.
This PROVn framework is also compatible with POLE principles. Using Neo4j we can quickly and efficiently identify and notify Persons, Objects, Locations and Entities to be shared with health officials and sanitary/policital resources to identify and map areas of concern and ring/risk patterns.
The POLE data model — Person, Object, Location, Event — is commonly applied to security and investigative use cases such as policing, anti-terrorism, border control, and social services. It’s also a great fit for the graph and graph algorithms. POLE data model can support police and social services investigations and generate real-time insights using the Neo4j browser as well as some sample visualisations. Some of the cases are to be found in police forces, government (tax / social service) agencies, immigration authorities, etc. They all have that same requirement of being able to analyse and link different entities together.

This database is built based on the combination of different data sources:
User-provided data by surveys of affected persons.
Official epidemiological data from the Epidemic Steering Committee of each region, departament or sanitary administration.
Social media data from participating partners, using a voluntary App downloaded by participants of a muestral epidemic program.
Other resorces by APIs or ETL processes.
Use Cases:
It provides a unique traceability model between the epidemiological alert trigger event, the confinement orders, identification of risk locations, identification of potential affected and infected individuals, evolution of their clinical state and result of PCR or similar tests, traceability of movements and allocation of agents of compliance with specific protocol, and its impact on the health system, its diagnosis, analysis, evolution of clinical history and knowledge base with all this repository of events and data that provides information to genetic research of the virus, its immunization, antibodies and possible mutation.
This project aids to contact tracing and smart quarantine in the context of the current coronavirus pandemic, identify people at risk using actual and potential contact tracing, suggest who should be informed or quarantined, visually explain why someone is at risk, find quarantine offenders. In resume, build intelligent systems upon the combined power of collaborative knowledge graphs and machine learning:
Pandemic workflow analysis: w/load real time data & get historical traceability.
Algoritm community & GIS distance for determine vulnerability/risk area with infectious potential.
Machine Learning algoritms applied to miminize impact based on behavioural patterns in descalate confinement and aids the researching of virus genoma.
Aids on Mitigation Strategy Political Programs.
Get efficient medical resources affectation of personnel, viral test kits, beds, respirators.
Clear definition of roles and responsibilities in extreme situations.
Manage monitoring of patient evolution and potential viral load of entities.
Scientific Investigation of mutations of virus strains. Will provide information that can be applied in analysis and the use of AI algorithms to assist in other anti-epidemic activities.
Propitiate complex scientific analysis and interdisciplinary collaboration about the pandemic phenomenon.
Simulate scenarios using agent-based modeling (Netlogo) generating PROV documents to feed back the graph base.
Correlate vaccins, clinic history and epidemiological deceases, aids to an effiient inmunization response of population groups and helps to medical programs.
Help government to localize, predict and prepare for quarantine or treatment of potentially infected individuals as well as disinfection of unsafe areas to prevent the rapid spread of the virus to the community.
Update interpersonal contacts, places and trips in the last days. It allows knowing the risk of infection at any geographic level or entity (institution) using community detection algorithms. Through daily updated information, governments are adequately prepared to face different situations and strategies of de-escalation and de-confinement.
Once the data — structured and unstructured — is converted into neo4j knowledge graph, the customizable and extensible platform helps to extract actionable insights and handle complex tasks like contextualize, explore, analyze, understand, and act upon vast amounts of information using the latest advances in graph analytics, and machine learning.
What is PROV and why it is useful for pandemic modeling?
Inspired in Stefan article: https://medium.com/neo4j/getting-started-with-provenance-and-neo4j-b50f666d8656
Provenance describes the origin and history of “a thing”. The term provenance originally has been used for paintings and their owner history over time. If there are some missing Provenance information, for example, a decade where you can’t tell who was the owner, the painting value drops immediately.
Today we use the term provenance to track processes and responsibilities in general. For example to track the production of food or to track the history of a file.
W3C — PROV standard: In 2003 the W3C adopted the official PROV standard to describe provenance structures. I don’t want to explain the complete standard only the key concepts: Entities, Activities, Agents, and Relations.
PROV and Neo4j
To handle PROV graphs it is useful to store the information in some kind of database instead of a single file. Neo4j provides the required features to store PROV data in a property graph:
Nodes — Mapped to Entities, Activities, and Agents
Relations — For example, used, wasGenerartedBy …
Properties — Predefined PROV — as well as custom properties can be attached to nodes as well as to relations (for example startAtTime, endAtTime)
Within all the information in the graph database, the analyst benefits from Cypher powerful query mechanisms to extract information for analyze and answer questions like:
What is the origin of this contagious spread?
Who was responsible for the confine and control of evolution of patient?
Is this patient under good treatment and quarentine conditions (based on evolution of the illness and clinical diagnostics) ?
When an individual is confirmed to be infected it could mark a risk indicator to all of the patient social contacts to allow other confine and protocol application.
When a flight, bus, building, hospital, residence, etc is confirmed to have passengers or residents infected , all passengers on that ambit, entity and zone with and their contacts are also found promptly.

When a place is confirmed to have people infected all people who arrive at the same time with the infected patient are immediately found.
All the evolution in the illness upon, their states, updating and risks are in continuous and online update in the database, for aids to a real time decision taking.
Resume:
We described a new tool to stop the spread of COVID-19, analyzing the types of contagious and confine patterns, for minimize social distancing also. If we could completely stop all interactions between people, this would be over very quickly. Unfortunately, to keep a country operational, we have people that still need to be moving around. Some of these people may be asymptomatic carriers or they may encounter someone who is. Anyone of us going to the grocery store, the doctors, to work may contribute to the virus’s transmission without even knowing it. To combat this, health officials need to trace the movements of anyone that tests positive, then all the people they encountered, and all the people encountered, and so on. This is difficult and time consuming. To assist with this, we need the support of thirty-party contact tracing app and online decentralizated survey to load data to this PROVn neo4j framework.
Also, research in Dependency Provenance in epidemiological spread and virus mutation using ABM for model and simulate scenarios provided by real time data by neo4j, is a must.
In resume, next and desired steps in the evolution of this proyect needs helping us in:
GIS layer visualization (for ex. Linkurious/neo4j)
Define a final COVID19 PROV Template and Bindings (and CSV/API structure)
Collaboration in provide CSVs/APIs data with real cases from Sanitary Institutions, Google Maps, etc.
Standardize collect data for: Mobile Apps and Surveys of affected people
Finantial support for continue reserching in this proyect.
Links:
Graphs4good author presentation 27/03/2020:

2020-graphs4good-graphhack-projects showcase: Covid19_provenance_n: Social Provenance and Graph Spread Using Neo4j & PROV
https://neo4j.com/blog/2020-graphs4good-graphhack-projects/