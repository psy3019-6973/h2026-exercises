🧠 Stroop Task Experiment

PhD Research Project — Pierre-Antoine [Last Name]

This repository contains the code, materials, and analysis pipeline for a doctoral research project investigating cognitive control and interference processing using a computerized Stroop task.

📌 Project Overview

The Stroop task is a classic paradigm in cognitive psychology used to measure attentional control, processing speed, and interference resolution.

In this project, we use behavioral measures (reaction time and accuracy) to examine:

Cognitive control mechanisms

Individual differences in interference susceptibility

The relationship between response conflict and decision latency

This experiment is part of Pierre-Antoine's PhD thesis in psychology.

🧪 Experimental Design

Participants are asked to identify the font color of a displayed word while ignoring the word's semantic meaning.

Condition	Example	Description
Congruent	RED (in red)	Word meaning and font color match
Incongruent	RED (in blue)	Word meaning and font color conflict
Neutral	XXXX (in green)	No semantic interference
Measures Collected

Reaction time (ms)

Response accuracy

Trial type (congruent / incongruent / neutral)

💻 Task Implementation

The experiment is implemented using:

PsychoPy / PsychoJS

Python for local testing

JavaScript for online deployment

Stimuli presentation and response collection are fully automated.

📂 Repository Structure
stroop-task/
│
├── experiment/          # Task code (PsychoPy / PsychoJS)
├── stimuli/             # Word and color stimulus definitions
├── data/                # Raw participant data (excluded from repo)
├── analysis/            # Scripts for preprocessing and statistics
├── results/             # Output figures and statistical results
└── README.md            # Project documentation

▶️ Running the Experiment
Local (Python / PsychoPy)
python experiment/stroop_experiment.py

Online (PsychoJS)

Upload the html/ folder to Pavlovia or another compatible server.

📊 Data Analysis

Analysis scripts are written in Python and R.

Main steps:

Remove incorrect trials

Exclude reaction times < 200 ms or > 3000 ms

Compute mean RT per condition

Calculate Stroop interference effect:

Interference = RT_incongruent - RT_congruent

🔒 Ethics

This study follows institutional ethical guidelines.
All participants provide informed consent before participation.
No personally identifying information is stored in this repository.

📖 Thesis Context

This project contributes to a broader investigation of:

Cognitive control

Attention and conflict monitoring

Behavioral markers of executive function

👨‍🔬 Author

Pierre-Antoine [Last Name]
PhD Candidate in Psychology
[University Name]

📬 Contact

For questions about the experiment or collaboration inquiries, please contact:
pierre-antoine@university.edu
