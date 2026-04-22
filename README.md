# 📊 Customer Churn Prediction
### Telecom Customer Analysis using Logistic Regression

---

## 🎯 Problem Statement

A telecom company is losing customers (churning) every month, directly impacting revenue.  
This project builds a machine learning model to **predict which customers are likely to churn**, enabling the business to take proactive retention actions.

---

## 📁 Project Structure

```
customer_churn_project/
│
├── telecom_churn.csv                   # Dataset (1,000 customers, 17 features)
├── Customer_Churn_Prediction.ipynb     # Main Jupyter Notebook (full analysis)
├── README.md                           # Project documentation
│
├── plot1_churn_distribution.png        # Churn count & percentage
├── plot2_contract_churn.png            # Churn by contract type
├── plot3_tenure_churn.png              # Tenure distribution by churn
├── plot4_charges_churn.png             # Monthly charges vs churn
├── plot5_service_payment_churn.png     # Internet service & payment method
├── plot6_correlation_heatmap.png       # Feature correlation heatmap
├── plot7_confusion_matrix.png          # Model confusion matrix
├── plot8_roc_curve.png                 # ROC-AUC curve
└── plot9_feature_importance.png        # Logistic regression coefficients
```

---

## 📊 Dataset Overview

| Property | Value |
|---|---|
| Total Customers | 1,000 |
| Features | 17 |
| Churn Rate | ~24% |
| Target Variable | Churn (Yes / No) |

### Features include:
- **Demographics** — Gender, SeniorCitizen, Partner, Dependents
- **Services** — PhoneService, InternetService, OnlineSecurity, TechSupport
- **Account Info** — Tenure, Contract, PaymentMethod, MonthlyCharges, TotalCharges

---

## 🔧 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Pandas | Data loading & manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualizations |
| Scikit-learn | ML model, preprocessing & evaluation |

---

## 📌 Project Workflow

```
1. Load & Understand Data
        ↓
2. Exploratory Data Analysis (EDA)
        ↓
3. Data Preprocessing
   (Encoding → Scaling → Train-Test Split)
        ↓
4. Model Building
   (Logistic Regression)
        ↓
5. Model Evaluation
   (Accuracy, F1, ROC-AUC, Confusion Matrix)
        ↓
6. Business Insights & Recommendations
```

---

## 📈 Model Results

| Metric | Score |
|---|---|
| Accuracy | 76% |
| ROC-AUC | 0.77 |
| Precision (Churn) | 0.50 |
| Recall (Not Churn) | 0.97 |

---

## 💡 Key Insights

1. **Contract type** is the strongest churn predictor — month-to-month customers churn far more
2. **Short tenure** customers (< 12 months) are at highest risk
3. **Fiber optic** users churn more than DSL users — possibly due to higher charges
4. **Electronic check** payment correlates with higher churn
5. **High monthly charges** increase churn probability

---

## ✅ Business Recommendations

- Offer discounts to convert month-to-month customers to annual contracts
- Create loyalty rewards for customers in their first 6 months
- Investigate fiber optic service quality and pricing
- Incentivize customers to switch to automatic payment methods

---

## 🚀 How to Run

```bash
# 1. Clone or download this project folder

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# 3. Open the notebook
jupyter notebook Customer_Churn_Prediction.ipynb

# OR run as a Python script
python run_project.py
```

---

## 👤 Author

**Kshirsagar Mahesh S.**  
B.E. in Artificial Intelligence & Data Science  
📧 maheshkshirsagar510@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/mskshirsagar) | [GitHub](https://github.com/mayu510)
