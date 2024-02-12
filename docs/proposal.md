## 1. **Predicting Diabetes Risk**
- Prepared for UMBC Data Science Master Degree Capstone by **Dr Chaojie (Jay) Wang**
- Shankara Parameshwari Navya Sri Dameruppula
- GitHub profile : https://github.com/dspnavyasri
- LinkedIn progile : https://www.linkedin.com/in/shankara-parameshwari-navya-sri-dameruppula-a8697b239/
- PowerPoint :
- YouTube video :
    
## 2. Background

- What is it about?
- Diabetes is a prevalent chronic disease affecting millions worldwide. Early detection and intervention can significantly improve patient outcomes and reduce healthcare costs. In this project, we aim to leverage machine learning techniques to predict the risk of diabetes based on various health metrics and lifestyle factors.

- Why does it matter?
- Early prediction of diabetes risk can enable targeted preventive measures and personalized interventions, potentially reducing the incidence of diabetes-related complications and improving overall health outcomes for individuals at risk.
  
- What are your research questions?
1. Can we accurately predict the risk of developing diabetes based on demographic information and health indicators?
2. Which machine learning algorithms perform best in predicting diabetes risk?
3. How do different features contribute to the prediction of diabetes risk?

## 3. Data 

Describe the datasets you are using to answer your research questions[.
- Data sources : (https://www.kaggle.com/datasets/shantanudhakadd/diabetes-dataset-for-beginners)
- Data size : 40KB
- Data shape (number of rows and columns): 768 rows and 9 columns

### Loan Dataset Data Dictionary

| Column Name            | Data Type | Definition                                            | Potential Values         |
|------------------------|-----------|------------------------------------------------------|--------------------------|
| Pregnancies            | Integer   | Number of pregnancies                                | 0, 1, 2, ...             |
| Glucose                | Integer   | Plasma glucose concentration 2 hours in an oral glucose tolerance test |                          |
| BloodPressure          | Integer   | Diastolic blood pressure (mm Hg)                     |                          |
| SkinThickness          | Integer   | Triceps skin fold thickness (mm)                     |                          |
| Insulin                | Integer   | 2-Hour serum insulin (mu U/ml)                       |                          |
| BMI                    | Float     | Body mass index (weight in kg/(height in m)^2)       |                          |
| DiabetesPedigreeFunction | Float   | Diabetes pedigree function                           |                          |
| Age                    | Integer   | Age (years)                                          |                          |
| Outcome                | Integer   | Class variable (0 or 1) indicating diabetes or not   | 0 - No diabetes, 1 - Diabetes |



- Which variable/column will be your target/label in your ML model?
- "Outcome" variable will be the target or label in the machine learning model. This column indicates whether a person has diabetes or not, with the values 0 representing "No diabetes" and 1 representing "Diabetes".


- Which variables/columns may be selected as features/predictors for your ML models?
1. Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age

This structured dataset provides valuable insights into various health indicators and demographic information, which can be utilized to train machine learning models for predicting diabetes risk.


