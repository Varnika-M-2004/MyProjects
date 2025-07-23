
# Panic Disorder Prediction using Machine Learning

This project aims to predict **Panic Disorder Diagnosis** using a dataset of 20,000 participants containing clinical, demographic, and lifestyle features. Multiple machine learning models were trained and evaluated to achieve high prediction accuracy.

---

## Dataset Overview

- **Rows:** 20,000
- **Columns:** 17
- **Features include:**
  - Age, Gender
  - Family/Personal Medical History
  - Current Stressors, Symptoms, Severity
  - Demographics, Lifestyle Factors
  - Target: `Panic Disorder Diagnosis (0 = No, 1 = Yes)`

---

##Models Used

- Decision Tree
- Random Forest
- XGBoost
- Voting Classifier (Ensemble)

---

## Results

| Model               | Accuracy | F1-Score |
|---------------------|----------|----------|
| Decision Tree       | 86%      | 0.65     |
| Random Forest       | 100%     | 1.00     |
| XGBoost             | 100%     | 1.00     |
| Voting Classifier   | 100%     | 0.98     |

- **Best Model:** Random Forest & XGBoost (100% Accuracy)
- **Cross-Validation Mean Accuracy:** 99%
- **Bias:** 4150.696  
- **Variance:** ~0

---

## Contact
For questions or feedback, reach out:  
varni.mulay@gmail.com  
[LinkedIn](https://www.linkedin.com/in/varnika-mulay)
