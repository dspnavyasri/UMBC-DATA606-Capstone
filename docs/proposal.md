## 1. **Loan Approval Prediction**
- Prepared for UMBC Data Science Master Degree Capstone by **Dr Chaojie (Jay) Wang**
- Shankara Parameshwari Navya Sri Dameruppula
- GitHub profile : https://github.com/dspnavyasri
- LinkedIn profile : https://www.linkedin.com/in/shankara-parameshwari-navya-sri-dameruppula-a8697b239/

    
## 2. Background

- What is it about?
- Dataset is related to loan applications, where various attributes of applicants are recorded along with the outcome of the loan application.
  **Loan approval** is a process where a financial institution, such as a bank or a lending company, evaluates an individual's or a business's application
  for a loan and decides whether to grant the requested loan amount. Understanding and analyzing these factors in a loan dataset can help identify
  patterns and build predictive models to automate the loan approval process, making it more efficient and consistent.

- Why does it matter?
- Loan prediction is crucial for financial institutions to assess the risk associated with granting loans.
  Understanding the patterns in the dataset can help in creating predictive models to automate decision-making in loan approvals.
  
- What are your research questions?
1. What factors contribute most to loan approval or rejection?
2. How does credit history impact the likelihood of loan approval?
3. Are there any patterns in the income and loan amount requested by applicants?
4. How does marital status or education level influence loan approval?
and many more... We can gain insights into the key factors affecting loan approvals and potentially build predictive models for future loan applications.

## 3. Data 

Describe the datasets you are using to answer your research questions.
- Data sources : https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset
- Data size : 40KB
- Data shape (# of rows and # columns) : 614 of rows and 13 columns
  
### Loan Dataset Data Dictionary

| Column Name         | Data Type | Definition                                   | Potential Values                 |
|---------------------|-----------|----------------------------------------------|----------------------------------|
| Loan_ID             | Object    | Unique identifier for each loan application  |                                  |
| Gender              | Object    | Gender of the applicant                      | Male, Female                     |
| Married             | Object    | Marital status of the applicant              | Yes, No                          |
| Dependents          | Object    | Number of dependents                         | 0, 1, 2, 3+                      |
| Education           | Object   | Education level of the applicant             | Graduate, Not Graduate           |
| Self_Employed       | Object    | Indicates whether the applicant is self-employed | Yes, No                       |
| ApplicantIncome     | Int64     | Income of the applicant                      |                                  |
| CoapplicantIncome   | Float64   | Income of the co-applicant (if any)          |                                  |
| LoanAmount          | Float64     | The amount of the loan applied for           |                                  |
| Loan_Amount_Term    | Float64     | The term (in months) for which the loan is applied |                              |
| Credit_History      | Float64     | Credit history of the applicant              | 1 (Good), 0 (Bad)               |
| Property_Area       | Object    | Area where the property is located           | Urban, Semiurban, Rural          |
| Loan_Status         | Object    | The final status of the loan application (target variable) | Y (Approved), N (Not Approved) |

- Which variable/column will be your target/label in your ML model?
- The goal is to predict whether a loan application will be approved or not, the most suitable
  target or label variable for the machine learning model would be the **Loan_Status** column.
  This column indicates the final status of the loan application and can take on values like 'Y' (Approved) or 'N' (Not Approved).
  
- Which variables/columns may be selected as features/predictors for your ML models?
1. **Gender**: The gender of the applicant.
2. **Married**: Marital status of the applicant.
3. **Dependents**: Number of dependents.
4. **Education**: Education level of the applicant.
5. **Self_Employed**: Indicates whether the applicant is self-employed.
6.**ApplicantIncome**: Income of the applicant.
7. **CoapplicantIncome**: Income of the co-applicant (if any).
