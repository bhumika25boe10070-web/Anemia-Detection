# Anemia Severity Prediction Using Machine Learning

This project was created as part of the Fundamentals of AI & ML course. The aim is to predict anemia severity (Normal, Mild, Moderate, Severe) using routine CBC parameters. Since anemia is common and CBC tests are easily available, the idea was to train a simple ML model that can give a quick estimate of severity based on basic blood values.

## Overview
The project uses synthetic tabular data, performs preprocessing, trains a multiclass classification model, and then allows predictions through a simple Python script. All related files such as the dataset, model files, diagrams, screenshots, and project report are included inside the project folder.

## Project Structure
Anemia-ML-Project/
│
├── DATA/
│ ├── raw.csv
│ └── processed.csv
│
├── src/
│ ├── data_prep.py
│ ├── train.py
│ ├── predict.py
│ └── init.py
│
├── MODELS/
│ ├── anemia_model.pkl
│ └── scaler.pkl
│
├── DIAGRAMS/
│ ├── UML, SEQUENCE & CLASS DIAGRAMS.png
│ └── WORKFLOW DIAGRAM.png
│
├── SCREENSHOTS/
│ ├── DATA_PREP.png
│ ├── TRAINING.png
│ ├── PREDICT.png
│ └── dataset_preview.png
│
├── PROJECT REPORT/
│ └── Anemia Project Report.pdf
│
├── README.md
└── statement.md

## How to Run
1. Install requirements:
2. Preprocess the data:
3. Train the machine learning model:
4. Make a prediction:

## Technologies Used
- Python  
- pandas, numpy  
- scikit-learn  
- joblib  
- matplotlib  
- UML diagram tools

## Features
- Reads CBC values and preprocesses them  
- Trains a multiclass machine learning model  
- Saves trained model + scaler  
- Simple prediction script for testing  
- Includes diagrams and screenshots for documentation  

## Model Evaluation
The model was validated with:
- Train-test split  
- Confusion matrix  
- Basic classification metrics  

The required screenshots are included in the **SCREENSHOTS** folder.

## Note
The dataset used is completely synthetic and only for academic purposes. No personal or clinical records are used.
