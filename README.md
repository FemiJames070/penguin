# 🐧 Penguin Species Predictor: Interactive ML Application

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Live App](https://img.shields.io/badge/Live_App-View_Here-2e7d32?style=flat)](https://penguin-xhsre9nwnjmgd5nfmd5g3v.streamlit.app/)

## 🚀 Live Application
**Experience the interactive dashboard here:** [Penguin Predictor Web App](https://penguin-xhsre9nwnjmgd5nfmd5g3v.streamlit.app/)

## 📖 Overview
This repository contains a data-driven web application that integrates machine learning directly into an interactive user interface. Built with **Streamlit**, the application utilizes a **Random Forest Classifier** to predict the species of a penguin (Adelie, Chinstrap, or Gentoo) based on geographical data and morphological measurements.

This project demonstrates the end-to-end integration of raw data ingestion, real-time user input, on-the-fly model training, and probabilistic inference—all wrapped in a clean, accessible web dashboard.

## ✨ Key Features
* **Interactive Feature Input:** A dynamic sidebar allows users to adjust continuous variables (bill length, body mass, etc.) and categorical variables (island, gender) in real-time.
* **Automated Data Pipeline:** The app automatically handles data ingestion, dynamic feature encoding (`pd.get_dummies`), and matrix preparation for the machine learning model.
* **Integrated Visualization:** Utilizes **Altair** to generate interactive scatter plots, allowing users to visually explore the relationship between body mass, bill length, and species.
* **Probabilistic Inference:** Instead of just outputting a single prediction, the app displays the prediction probabilities for all three species using custom UI progress bars.

## 🛠️ Technology Stack
* **Language:** Python 3.10+
* **Web Framework:** Streamlit
* **Machine Learning:** Scikit-Learn (RandomForestClassifier)
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Altair

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/penguin-predictor-app.git](https://github.com/yourusername/penguin-predictor-app.git)
   cd penguin-predictor-app

2. **Install the required dependencies:**
   ```bash
   pip install streamlit numpy pandas scikit-learn altair
   Run the Streamlit App:

   ```bash
   streamlit run app.py

3. **Access the Dashboard:**
Open your browser and navigate to the local URL provided in your terminal (usually http://localhost:8501).

✍️ Author
Femi James Data & Business Analyst | Integrated AI Specialist
