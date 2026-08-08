# Heart Disease Risk Prediction

An end-to-end machine learning project that predicts a patient's risk of heart disease based on clinical parameters, deployed as both a REST API and an interactive web app.

## Problem Statement

Cardiovascular disease is one of the leading causes of death worldwide. Early risk detection using clinical data can help doctors prioritize further testing and intervention. This project builds a machine learning model that estimates a patient's heart disease risk from basic clinical measurements, and wraps it in a usable application.

## Dataset

- **Source:** [Heart Failure Prediction Dataset (Kaggle)](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
- 918 patient records with 11 clinical features (age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, resting ECG, max heart rate, exercise-induced angina, oldpeak, ST slope) and a binary target (presence of heart disease).

## Approach

1. **Exploratory Data Analysis** — checked for missing values, class balance, and feature correlation with the target.
2. **Preprocessing** — encoded categorical features, split data into train/test sets (80/20, stratified).
3. **Model Training & Comparison** — trained and evaluated three models: Logistic Regression, Random Forest, and XGBoost.
4. **Model Selection** — selected the best model based on **recall**, since in a medical screening context, missing a positive case (false negative) is more costly than a false alarm.
5. **API** — built a REST API with FastAPI that serves predictions from the trained model.
6. **Web App** — built an interactive Streamlit interface so a user can enter patient details and get an instant risk assessment.

## Results

| Model | Accuracy | Recall | ROC-AUC |
|---|---|---|---|
| Logistic Regression | 0.875 | **0.931** | 0.868 |
| Random Forest | 0.875 | 0.902 | 0.872 |
| XGBoost | 0.870 | 0.863 | 0.870 |

**Selected model: Logistic Regression** — highest recall (93.1%), meaning it catches the highest proportion of actual heart disease cases, which is the priority metric for this use case.

## Screenshots

**High Risk Prediction**
![High Risk](screenshots/high_risk_result.png)

**Low Risk Prediction**
![Low Risk](screenshots/low_risk_result.png)

## For Non-Medical Readers (Feature Glossary)

If you're not from a medical background, here's a plain-language explanation of the input features, using a systems-monitoring analogy:

Think of the human heart like a server you're monitoring — each feature below is basically a sensor reading. The model looks for patterns across these readings that resemble "systems heading toward failure" versus "healthy systems."

**Chest Pain Type** — Was there a warning sign, and what kind?
- `TA` (Typical Angina) — a clear, expected warning signal, classic heart-related pain
- `ATA` (Atypical Angina) — an ambiguous signal, might be heart-related, might not
- `NAP` (Non-Anginal Pain) — pain exists, but unrelated to the heart (a false alarm, essentially)
- `ASY` (Asymptomatic) — **no warning at all**, even though a problem may exist. This is the most dangerous case — like a server silently failing with no error logged until it crashes. It's the strongest risk indicator in the data.

**Resting ECG** — A "log file" of the heart's electrical activity while idle (patient at rest)
- `Normal` — no errors in the log
- `ST` — a specific abnormal signal pattern detected
- `LVH` — the heart's main pumping chamber has thickened over time, similar to a motor that's been overworked and physically strained from years of extra load (usually caused by long-term high blood pressure)

**Exercise-Induced Angina** — Simple yes/no: did pain appear under physical load (like a stress test on a system)?

**Oldpeak** — A numeric deviation score measuring how much the heart's electrical signal dips during exercise compared to resting baseline. Higher = bigger abnormal deviation under load, similar to a latency spike during load testing — a small spike is normal, a large one signals trouble.

**ST Slope** — The shape/trend of that signal right after peak exertion
- `Up` — signal recovers well (healthy pattern)
- `Flat` — signal plateaus, doesn't recover well (mild warning sign)
- `Down` — signal declines (strongest warning sign)

**Fasting Blood Sugar** — A simple threshold flag: `1` if blood sugar is above 120 mg/dl (a diabetes-related risk marker), `0` if below.

**In short:** this model performs anomaly detection on 11 "health metrics" to classify whether the overall pattern looks like a system trending toward failure (heart disease) or a healthy one — the same way a monitoring dashboard flags "this server is likely to crash soon" based on CPU, memory, and error-log trends.

## Tech Stack

- **Language:** Python
- **ML/Data:** pandas, scikit-learn, XGBoost, joblib
- **API:** FastAPI, Uvicorn
- **Web App:** Streamlit

## Project Structure