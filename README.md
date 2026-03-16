# 🚦 AI City Traffic Intelligence System

![Project Banner](https://raw.githubusercontent.com/peanutpirate/AI_City_Traffic_Intelligence_System/main/project_banner.png)

An end-to-end **Data Science and AI project** that analyzes city traffic patterns and predicts future traffic volume using machine learning.

The system combines **data analysis, feature engineering, visualization, and neural network prediction** to estimate traffic congestion levels and calculate a traffic risk score.

This project demonstrates how data science techniques can be applied to **urban mobility and traffic intelligence systems**.

---

# 📊 Project Overview

Urban traffic congestion is a growing challenge in modern cities.  
Understanding traffic patterns and predicting future traffic volume can help city planners and transportation systems improve road efficiency and reduce congestion.

This project analyzes traffic data and builds an AI model capable of:

• Detecting traffic patterns across hours and days  
• Understanding weather impact on traffic volume  
• Predicting future traffic volume using TensorFlow  
• Calculating a traffic **risk score** for congestion

---

# 🧠 Key Features

✔ Exploratory Data Analysis (EDA)  
✔ Feature Engineering  
✔ Traffic Pattern Visualization  
✔ Neural Network Traffic Prediction  
✔ Traffic Risk Scoring System  

---

# 📂 Project Structure
    traffic-ai-system/

data/
traffic.csv

src/
data_loader.py
preprocessing.py
feature_engineering.py
visualization.py
traffic_model.py
risk_analyzer.py

models/
traffic_model.h5

main.py
README.md

---

# 📊 Dataset

This project uses a public traffic dataset from Kaggle.

Example datasets:

Traffic Prediction Dataset  
https://www.kaggle.com/datasets/hasibullahaman/traffic-prediction-dataset

Alternative dataset:

Metro Interstate Traffic Volume  
https://www.kaggle.com/datasets/utkarshxy/metro-interstate-traffic-volume

Dataset features include:

• Date and time  
• Weather conditions  
• Temperature  
• Rain / Snow information  
• Traffic volume

---

# 🔎 Exploratory Data Analysis

The first stage of the project focuses on understanding traffic behavior.

Key questions explored:

• At what hours is traffic most intense?  
• Which days have the highest traffic volume?  
• How does weather affect traffic patterns?

# 🧪 Feature Engineering

New features were created to improve model performance:

• `hour` — hour of the day  
• `day_of_week` — weekday indicator  
• `is_weekend` — weekend flag  
• `weather_score` — simplified weather impact indicator  

Feature engineering helps the model better understand traffic patterns and temporal behavior.

---

# 🤖 Traffic Prediction Model

A neural network built using **TensorFlow / Keras** predicts future traffic volume.

Model architecture:

Input Features
↓
Dense Layer (64 neurons)
↓
Dense Layer (32 neurons)
↓
Output Layer (Traffic Volume Prediction)


The model learns relationships between time, weather conditions, and traffic flow.

---

# 🚨 Traffic Risk Score System

To make the system more practical, a **traffic risk score** was implemented.

The risk score considers:

• predicted traffic volume  
• weather conditions (rain)  
• time of day

Example output:

Time: 18:00
Weather: Rain
Predicted Traffic Volume: 6200

Traffic Risk Level → HIGH


This component simulates how an intelligent traffic monitoring system might classify congestion risk.

---

# 📊 Visualizations

The project generates several key visualizations:

Traffic Volume by Hour  
Traffic Volume by Day of Week  
Weather Impact on Traffic  
Traffic Distribution

These graphs help identify patterns and support model interpretation.

---

# ⚙️ How to Run the Project

Clone the repository
git clone https://github.com/yourusername/traffic-ai-system.git


Navigate to the project directory


cd traffic-ai-system


Install dependencies


pip install -r requirements.txt


Run the system


python main.py


---

# 📈 Example Prediction

Example system output:


Input
Hour → 18
Rain → Yes
Day → Monday

AI Prediction
Traffic Volume → 6200

Risk Level → HIGH


---

# 📘 What This Project Demonstrates

This project demonstrates several key data science skills:

• Exploratory data analysis  
• Feature engineering  
• Machine learning modeling  
• Neural network prediction  
• Data visualization  
• Practical system design

---

# 🚀 Future Improvements

Possible improvements include:

• LSTM time-series traffic prediction  
• Real-time traffic API integration  
• Interactive dashboard (Streamlit / Dash)  
• Traffic anomaly detection  
• Smart traffic alert system

---

# 👩‍💻 Author

Built as part of the **#66DaysOfData learning journey** by Ipek EGMEN.
