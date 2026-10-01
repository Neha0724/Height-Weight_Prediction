# Height & Weight Prediction

A Machine Learning project that predicts **weight based on height** using regression models and a Streamlit web application.

## Project Structure

```text
height-weight-prediction/
│
├── app.py
├── best_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.11
- Streamlit
- Pandas
- Scikit-learn 1.6.1
- Joblib

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Go to the project folder

```bash
cd height-weight-prediction
```

### 3. Check Python version

```bash
py -3.11 --version
```

Expected output:

```text
Python 3.11.x
```

### 4. Install required packages

```bash
py -3.11 -m pip install -r requirements.txt
```

## Run the Streamlit App

Run:

```bash
py -3.11 -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

If it does not open automatically, copy the URL into your browser.

## Machine Learning Model

The project uses a trained regression model stored in:

```text
best_model.pkl
```

The scaler used during model training is stored in:

```text
scaler.pkl
```

The Streamlit application loads these files and uses them to predict weight from the height entered by the user.

## Prediction Flow

```text
User enters Height
        ↓
Streamlit Application
        ↓
Scaler (if required)
        ↓
Trained ML Model
        ↓
Predicted Weight
```

## Quick Start

If you already have the project folder:

```bash
cd height-weight-prediction
py -3.11 --version
py -3.11 -m pip install -r requirements.txt
py -3.11 -m streamlit run app.py
```

## Stop the Application

To stop the Streamlit application, press:

```text
Ctrl + C
```