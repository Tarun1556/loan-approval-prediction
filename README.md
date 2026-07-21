# Loan Approval Prediction

## Summary
Loan Approval Prediction is a Python-based machine learning application that predicts loan eligibility from applicant data. The project includes data preprocessing, feature engineering, model training, evaluation, and a Streamlit-based dashboard for real-time user interaction.

## Key Contributions
- Designed and implemented a complete end-to-end loan approval prediction pipeline
- Preprocessed data and engineered features for improved model accuracy
- Trained and evaluated a Random Forest classification model achieving 95.78% accuracy
- Built a responsive Streamlit front end for collecting user inputs and displaying predictions
- Integrated model inference with a clean user interface for real-time decision support

## Technical Skills
- Python
- Scikit-learn
- Random Forest
- Pandas
- NumPy
- Streamlit
- Data preprocessing
- Model evaluation

## Features
- User input form for applicant details
- Real-time loan approval prediction
- Data preprocessing and feature engineering
- Model training and validation
- Easy deployment with Streamlit

## Project Structure
```
loan-approval-prediction/
├─ backend/
│  ├─ train_model.py         # model training and evaluation
│  ├─ preprocess.py         # data cleaning and feature engineering
│  ├─ predict.py            # model inference for live predictions
│  └─ dataset/
│     └─ loan_approval_dataset.csv
├─ frontend/
│  ├─ app.py                # Streamlit application front end
│  └─ requirements.txt      # required Python packages
└─ README.md                # project overview and usage instructions
```

## Setup and Run
1. Create a Python virtual environment
2. Install dependencies from `frontend/requirements.txt`
3. Run the Streamlit app:
   ```bash
   streamlit run frontend/app.py
   ```

## Outcome
Delivered a predictive analytics solution for loan approval decisions, supporting improved user experience and faster eligibility assessment through automation and interactive visualization.
