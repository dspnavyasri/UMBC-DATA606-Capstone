## 1. **Predicting Diabetes Risk**
- Author - Shankara Parameshwari Navya Sri Dameruppula
- Semester - Spring'24
- Prepared for UMBC Data Science Master Degree Capstone by **Dr Chaojie (Jay) Wang**
- GitHub profile : https://github.com/dspnavyasri
- LinkedIn progile : https://www.linkedin.com/in/shankara-parameshwari-navya-sri-dameruppula-a8697b239/
- PowerPoint :[https://github.com/dspnavyasri/rought-work/blob/main/docs/Predicting Diabetes Using Machine Learning .pptx](https://github.com/dspnavyasri/rought-work/blob/main/docs/Presentation.pptx)
- YouTube video : https://www.youtube.com/watch?v=jEeY6cHDm7A
  
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
- Data size : 25KB
- Data shape (number of rows and columns): 768 rows and 9 columns
### Diabetes Dataset Data Dictionary

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
## 4. Exploratory Data Analysis
There are no missing values and duplicate rows in the dataset. 

### Summary Statistics:

**Key Variables:**

- **Pregnancies:**
  - Minimum: 0
  - Maximum: 17
- **Glucose:**
  - Minimum: 0
  - Maximum: 199
- **Blood Pressure:**
  - Minimum: 0
  - Maximum: 122
- **Skin Thickness:**
  - Minimum: 0
  - Maximum: 99
- **Insulin:**
  - Minimum: 0
  - Maximum: 846
- **BMI:**
  - Minimum: 0
  - Maximum: 67.1
- **Diabetes Pedigree Function:**
  - Minimum: 0.078
  - Maximum: 2.42
- **Age:**
  - Minimum: 21
  - Maximum: 81
- **Outcome (Target Variable):**
  - Minimum: 0
  - Maximum: 1
### Visualizations
**Distribution of Numerical Features.**
![1](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/1.png)
The graph shows the distribution of various numerical features in the dataset related to diabetes risk prediction. Each subplot represents a different feature, including the number of pregnancies, glucose levels, blood pressure, skin thickness, insulin levels, body mass index (BMI), diabetes pedigree function, and age.

These histograms display the frequency distribution of values within each feature, with the density curve overlaid (if kde=True). This visualization helps to understand the spread and central tendency of each feature, providing insights into the range and distribution of the data, which is crucial for feature understanding and selection in machine learning models.

**Outcome countplot.**
![2](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/2.png)
The countplot shows a relatively balanced distribution of outcomes, with a slightly higher number of non-diabetic individuals compared to diabetic individuals.

**Pairplot with Outcome Comparison.**
![3](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/3.png)
This visualization presents a comprehensive overview of the dataset's features and their relationships, considering the presence or absence of diabetes as denoted by the 'Outcome' column. Each feature is plotted against every other feature in a grid of scatterplots, providing insights into potential patterns, correlations, and separations between individuals with and without diabetes.

The diagonal plots display the distribution of each feature, while off-diagonal plots showcase the relationship between pairs of features. By coloring the data points based on the 'Outcome' column, where '0' signifies no diabetes and '1' indicates diabetes, the pairplot allows for a visual examination of how different features may be associated with the presence or absence of diabetes.

**Boxplot Analysis.**
![4](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/4.png)
This visualization presents boxplots for each feature in the dataset, providing insights into the distribution of data and the presence of potential outliers. Boxplots display the median, quartiles, and outliers, allowing for a quick understanding of the spread and central tendency of each feature's values.

By analyzing these boxplots, one can identify variations in feature distributions and assess whether certain features exhibit significantly different distributions between individuals with and without diabetes. The rotation of x-axis labels enhances readability, particularly when dealing with a large number of features.

**Heatmap**
![5](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/5.png)
correlation coefficient close to 1 indicates a strong positive correlation, meaning that as one feature increases, the other tends to increase as well. A correlation coefficient close to -1 indicates a strong negative correlation, meaning that as one feature increases, the other tends to decrease. A correlation coefficient close to 0 indicates little to no linear relationship between the features.

The annotations on the heatmap display the correlation values for better interpretation. The color palette 'coolwarm' is used to visualize positive and negative correlations distinctly, with warmer colors indicating positive correlations and cooler colors indicating negative correlations.

Glucose levels have a strong positive correlation with the outcome, indicating their importance in predicting diabetes risk.
Other features such as BMI and age also show moderate correlations with the outcome.

**Age vs. Glucose**
![6](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/6.png)
This line plot visualizes the average glucose levels across different age groups, segmented by diabetic status (Outcome). Each line represents the trend of average glucose levels for individuals with and without diabetes as age progresses.

The plot reveals how average glucose levels vary with age and diabetic status, providing insights into potential age-related patterns in glucose levels among diabetic and non-diabetic individuals. The separation or overlap of the lines indicates whether there are significant differences in glucose levels between the two outcome groups across different age groups.

Understanding these trends is crucial for assessing the impact of age on glucose levels and diabetes risk, which can inform strategies for diabetes management and prevention across different age demographics.

**Age Distribution by Outcome.**
![7](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/7.png)
This histogram illustrates the distribution of ages within the dataset, with each bar representing the count of individuals falling within specific age ranges. The histogram is color-coded by outcome, distinguishing between individuals with and without diabetes. We can clearly see that as we grow older in the 60+ age, there is not a big chance of not getting into diabetes. As we grow in mid 20-50 age. We might be prone to it but at later age can't find any such cases.

**BMI Distribution by Diabetes Outcome.**
![8](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/8.png)
![9](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/9.png)
This histogram visualizes the distribution of Body Mass Index (BMI) values within the dataset. Each bar represents the count of individuals falling within specific BMI ranges. The histogram is color-coded by outcome, distinguishing between individuals with and without diabetes. we can site this properly that below 20 age, its normal BMI results to no diabetes. but >20 BMI might hit or crate an impact on the body.

**Blood Pressure vs. Glucose.**
![10](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/10.png)
This visualization consists of two KDE (Kernel Density Estimation) plots, comparing the distributions of Blood Pressure and Glucose levels between diabetic and non-diabetic individuals.

Blood Pressure Distribution:

The left subplot showcases the KDE plots for Blood Pressure, with blue representing non-diabetic individuals and orange representing diabetic individuals. By observing the overlapping KDE curves, we can discern the density of blood pressure values for each group. Differences in the distributions may indicate potential associations between blood pressure levels and diabetes risk. Glucose Distribution:

The right subplot displays KDE plots for Glucose levels, with a similar color scheme distinguishing between diabetic and non-diabetic groups. These KDE curves offer insights into the distribution of glucose values across the two groups. Variations in the curves can suggest differences in glucose metabolism and its relationship with diabetes onset.

**Insulin vs. Glucose.**
![11](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/11.png)
Each bar represents the average value of Insulin and Glucose for the respective outcome category. The blue bars denote the average Insulin levels, while the orange bars represent the average Glucose levels. By comparing the heights of the bars within each outcome category, we can observe differences in average Insulin and Glucose levels between diabetic and non-diabetic individuals. Annotations atop each bar display the precise average values, providing further insights into the differences between the two outcome groups.

## 5. Model Training 
### Logistic Regression:
**Definition:** Logistic Regression is a statistical method used for binary classification tasks. It predicts the probability of occurrence of an event by fitting data to a logistic function, which outputs values between 0 and 1, representing the probability of the event.

**How it Works:** 
- In Logistic Regression, the input features are linearly combined with weights, and the logistic function (sigmoid function) is applied to the result. This transforms the output into probabilities. The model is trained using optimization techniques such as gradient descent to minimize the logistic loss function.

**Results:**

- Accuracy: 75%
- Recall: 80%
- F-1 Score: 81%
- Precision: 81%

### Random Forest:

**Definition:**  Random Forest is an ensemble learning method used for both classification and regression tasks. It constructs multiple decision trees during training and outputs the mode or mean prediction of the individual trees for classification or regression, respectively.

How it Works: 
- Random Forest builds multiple decision trees by randomly selecting subsets of features and data points. Each tree is trained independently, and the final prediction is made by aggregating the predictions of all trees (classification: mode, regression: mean).

**Results:**

- Accuracy: 75%
- Recall: 81%
- F-1 Score: 81%
- Precision: 81%

### Decision Tree:
**Definition:** A Decision Tree is a flowchart-like tree structure where each internal node represents a feature, each branch represents a decision rule, and each leaf node represents the outcome. It is a simple yet powerful non-linear model used for classification and regression tasks.

**How it Works:** 
- Decision Trees split the data into subsets based on the value of input features, aiming to maximize the homogeneity (purity) of the subsets regarding the target variable. This process is repeated recursively, creating a tree structure. During prediction, the input data traverse the tree from the root to a leaf node, which provides the final prediction.

**Results:**

- Accuracy: 76%
- Recall: 83%
- F-1 Score: 82%
- Precision: 80%

## 6. Application of the Trained Models
- Flask, a lightweight and versatile Python web framework, serves as the backbone for developing web applications, offering tools and libraries to swiftly create user interfaces, handle user input, and serve dynamic content. In the context of predicting diabetes risk from the dataset, Flask played a pivotal role in seamlessly integrating the trained machine learning models into a user-friendly web application. Through Flask, users interacted with features such as "Pregnancies," "Glucose Levels," "Blood Pressure," "Skin Thickness," "Insulin Levels," "BMI," "Diabetes Pedigree Function," and "Age" via an intuitive interface. This allowed the models to accurately predict users' risk of diabetes, based on their input data. By leveraging Flask's capabilities, the application facilitated informed decision-making, empowering users to proactively manage their health and well-being.

![12](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/12.png)
 
## 7. Conclusion
- This project focused on utilizing machine learning techniques, specifically logistic regression, random forest, and decision tree algorithms, to predict the risk of diabetes based on demographic information and health indicators. The integration of these models into a user-friendly web application powered by Flask facilitated easy access for users to input their data and obtain predictions regarding their diabetes risk. The potential applications of this project are significant, as early detection of diabetes risk can lead to targeted preventive measures and personalized interventions, ultimately improving patient outcomes and reducing healthcare costs.
![13](https://github.com/dspnavyasri/UMBC-DATA606-Capstone/blob/main/docs/13.png)

- ***Limitations:***
  - Despite its potential, this work has several limitations. Firstly, while the accuracy of the predictions achieved reasonable levels, it may not be sufficient for clinical diagnosis. Further validation with larger and more diverse datasets is necessary to enhance the reliability of the predictions. Additionally, the reliance on self-reported data and the absence of real-time monitoring capabilities may limit the application's effectiveness in certain contexts.


- ***Future Scope:***
  - Future research could explore several avenues to enhance the capabilities and effectiveness of the predictive models and web application. This includes integrating additional data sources such as genetic information or wearable device data to improve the predictive accuracy of the models. Moreover, incorporating feedback mechanisms and continuous improvement processes into the web application could further refine the accuracy and relevance of the predictions over time. Overall, this project lays the foundation for ongoing research and development efforts aimed at improving diabetes risk assessment and management through machine learning and web-based technologies.

## References
- Tasin, I., Nabil, T. U., Islam, S., & Khan, R. (2022). Diabetes prediction using machine learning and explainable AI techniques. Healthcare technology letters, 10(1-2), 1–10. https://doi.org/10.1049/htl2.12039.
- Fregoso-Aparicio, L., Noguez, J., Montesinos, L. et al. Machine learning and deep learning predictive models for type 2 diabetes: a systematic review. Diabetol Metab Syndr 13, 148 (2021). https://doi.org/10.1186/s13098-021-00767-9.
