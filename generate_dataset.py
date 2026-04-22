import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

# Customer demographics
customer_id = [f"CUST{str(i).zfill(4)}" for i in range(1, n+1)]
gender = np.random.choice(["Male", "Female"], n)
senior_citizen = np.random.choice([0, 1], n, p=[0.84, 0.16])
partner = np.random.choice(["Yes", "No"], n, p=[0.48, 0.52])
dependents = np.random.choice(["Yes", "No"], n, p=[0.30, 0.70])

# Service info
tenure = np.random.randint(1, 72, n)
phone_service = np.random.choice(["Yes", "No"], n, p=[0.90, 0.10])
multiple_lines = np.where(phone_service == "No", "No phone service",
                 np.random.choice(["Yes", "No"], n, p=[0.42, 0.58]))
internet_service = np.random.choice(["DSL", "Fiber optic", "No"], n, p=[0.34, 0.44, 0.22])
online_security = np.where(internet_service == "No", "No internet service",
                  np.random.choice(["Yes", "No"], n, p=[0.29, 0.71]))
tech_support = np.where(internet_service == "No", "No internet service",
               np.random.choice(["Yes", "No"], n, p=[0.29, 0.71]))

# Contract & billing
contract = np.random.choice(["Month-to-month", "One year", "Two year"], n, p=[0.55, 0.21, 0.24])
paperless_billing = np.random.choice(["Yes", "No"], n, p=[0.59, 0.41])
payment_method = np.random.choice(
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
    n, p=[0.34, 0.23, 0.22, 0.21]
)

# Charges — correlated with tenure and contract
monthly_charges = np.round(np.where(
    internet_service == "No", np.random.uniform(18, 35, n),
    np.where(internet_service == "DSL", np.random.uniform(45, 75, n),
             np.random.uniform(70, 110, n))
), 2)

total_charges = np.round(monthly_charges * tenure + np.random.uniform(-50, 50, n), 2)
total_charges = np.clip(total_charges, 0, None)

# Churn — higher for month-to-month, fiber, short tenure
churn_prob = (
    0.05
    + 0.30 * (contract == "Month-to-month")
    + 0.10 * (internet_service == "Fiber optic")
    + 0.15 * (tenure < 12)
    - 0.10 * (tenure > 36)
    + 0.08 * (payment_method == "Electronic check")
    - 0.08 * (online_security == "Yes")
    + 0.05 * (senior_citizen == 1)
)
churn_prob = np.clip(churn_prob, 0.03, 0.85)
churn = np.where(np.random.uniform(0, 1, n) < churn_prob, "Yes", "No")

df = pd.DataFrame({
    "CustomerID": customer_id,
    "Gender": gender,
    "SeniorCitizen": senior_citizen,
    "Partner": partner,
    "Dependents": dependents,
    "Tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "TechSupport": tech_support,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "Churn": churn
})

df.to_csv("/home/claude/customer_churn_project/telecom_churn.csv", index=False)
print(f"Dataset saved: {len(df)} rows, {df.columns.tolist()}")
print(f"Churn rate: {(df['Churn']=='Yes').mean()*100:.1f}%")
