"""
Women Socioeconomic Survey Data Generator

This script generates a realistic synthetic dataset representing
6,500 women's socioeconomic survey responses. The dataset is designed
for practicing data cleaning, SQL analysis, and Power BI visualization.

Author: SK
Tools: Python, NumPy, Pandas
"""


import numpy as np
import random
import pandas as pd

# Make results reproducible
np.random.seed(42)
rows = 6500
# -----------------------------
# Lists
# -----------------------------
counties = [
    "Nairobi","Kisii","Nakuru","Kisumu","Machakos",
    "Kakamega","Wajir","Mombasa","Nyeri","Narok"
]
marital_status = ["Married","Single","Widowed","Divorced"]
education = ["KCPE", "KCSE", "Certificate", "Diploma", "Graduate"]
occupation = ["Unemployed", "Farmer", "Small Business", "Casual Labour",
              "Vendor", "Civil servant", "fashion", "beauty", "Shop Attendant", 'corperative worker']
business_types = ["None", "Retail", "Agriculture", "food Vendoring", "beauty", "fashion", "cooperation", "Casual jobs"]
business_challenges = ["No Capital", "Low Customers", "High Competition", "Poor infrastructure", "High Taxes","No Challenge"]
yes_no = ["Yes","No"]

# -----------------------------
# Generating columns
# -----------------------------
participant_id = np.random.randint(100000,999999,rows)

age = np.random.triangular(23,43, 70, rows).astype(int)

county = np.random.choice(counties,rows)

marital = np.random.choice(marital_status, rows, p=[0.77,0.13,0.05,0.05])

education_level = np.random.choice(education, rows, p=[0.09,0.52,0.18,0.14,0.07])

occupation_col = []

for edu in education_level:
    if edu == "KCPE":
        occupation_col.append(np.random.choice(
            ["Farmer","Casual Labour","Vendor","Unemployed"],
            p=[0.45,0.25,0.15,0.15]))

    elif edu == "KCSE":
        occupation_col.append(np.random.choice(
            ["Farmer","Small Business","Vendor","Casual Labour","Unemployed"],
            p=[0.25,0.25,0.20,0.20,0.10]))

    elif edu == "Certificate":
        occupation_col.append(np.random.choice(
            ["Shop Attendant","beauty","fashion","Small Business"],
            p=[0.35,0.25,0.20,0.20]))

    elif edu == "Diploma":
        occupation_col.append(np.random.choice(
            ["Civil servant","corperative worker","Shop Attendant","Small Business"],
            p=[0.45,0.25,0.15,0.15]))

    else:
        occupation_col.append(np.random.choice(
            ["Civil servant","corperative worker","Small Business"],
            p=[0.60,0.20,0.20]))


#monthy income
monthly_income = []

for job in occupation_col:

    if job == "Unemployed":
        income = np.random.triangular(0,20,80)

    elif job == "Casual Labour":
        income = np.random.triangular(70,140,250)

    elif job == "Farmer":
        income = np.random.triangular(90,180,350)

    elif job == "Vendor":
        income = np.random.triangular(100,180,300)

    elif job == "Small Business":
        income = np.random.triangular(120,250,500)

    elif job == "Shop Attendant":
        income = np.random.triangular(120,180,300)

    elif job in ["beauty","fashion"]:
        income = np.random.triangular(100,220,450)

    else:
        income = np.random.triangular(250,450,700)

    monthly_income.append(int(income*100))

monthly_income = np.array(monthly_income)


monthly_savings = []
for pay in monthly_income:
    if np.random.rand() < 0.4:      # 40% save nothing
        monthly_savings.append(0)
    else:
        amount = pay * np.random.uniform(0.05, 0.20)
        monthly_savings.append(round(amount, -2))

monthly_savings = np.array(monthly_savings).astype(int)

saving_group = []

for amount in monthly_savings:
    if amount == 0:
        saving_group.append('No')
    else:
        saving_group.append(np.random.choice(['Yes','No'], p=[0.78, 0.22]))



owns_business = np.random.choice(yes_no, rows, p=[0.25,0.75])


business_type = np.where(owns_business == "Yes",np.random.choice(business_types[1:],rows,
        p=[0.17, 0.33, 0.07, 0.08, 0.10, 0.03, 0.22]),"None")

business_challenge = np.where(owns_business=="Yes", np.random.choice(business_challenges[:-1], rows),"No Challenge")

smartphone = []

for income in monthly_income:

    if income < 15000:
        smartphone.append(np.random.choice(["Yes","No"],p=[0.20,0.80]))

    elif income < 30000:
        smartphone.append(np.random.choice(["Yes","No"],p=[0.60,0.40]))

    else:
        smartphone.append(np.random.choice(["Yes","No"],p=[0.90,0.10]))

internet = []

for phone in smartphone:
    if phone == "Yes":
        internet.append(np.random.choice(["Yes", "No"], p=[0.80, 0.20]))
    else:
        internet.append(np.random.choice(["Yes", "No"], p=[0.05, 0.95]))
dependents = np.random.poisson(4,rows)

health_expense = np.random.triangular(10,15,30,rows)
health_expense = (health_expense*100).astype(int)

insurance = []

for income in monthly_income:

    if income < 15000:
        insurance.append(np.random.choice(["Yes","No"],p=[0.10,0.90]))

    elif income < 30000:
        insurance.append(np.random.choice(["Yes","No"],p=[0.35,0.65]))

    else:
        insurance.append(np.random.choice(["Yes","No"],p=[0.70,0.30]))


caregiving = np.random.randint(20, 61, rows)

training = np.random.choice(yes_no, rows, p=[0.23,0.77])


# -----------------------------
# Creating DataFrame
# -----------------------------

df = pd.DataFrame({
    "Participant ID":participant_id,
    "Age":age,
    "County":county,
    "Marital Status":marital,
    "Education Level":education_level,
    "Occupation":occupation_col,
    "Monthly Income":monthly_income,
    "Monthly Savings":monthly_savings,
    "Savings Group Member":saving_group,
    "Owns Business":owns_business,
    "Business Type":business_type,
    "Main Business Challenge":business_challenge,
    "Smartphone Access":smartphone,
    "Internet Access":internet,
    "Number of Dependents":dependents,
    "Monthly Health Expenses":health_expense,
    "Health Insurance":insurance,
    "Caregiving in hours/Week":caregiving,
    "Training Received":training
})

# Making data messy
# -----------------------------
# Missing values
for col in df.columns:
    df.loc[df.sample(frac=0.02).index,col] = np.nan

# Duplicate rows
duplicates = df.sample(100)
df = pd.concat([df,duplicates],ignore_index=True)

# Random extra spaces
df.loc[df.sample(80).index,"County"] = " Nairobi "
df.loc[df.sample(60).index,"Education Level"] = "KCSE "

# Mixed capitalization
df.loc[df.sample(70).index,"Health Insurance"] = "yes"
df.loc[df.sample(70).index,"Training Received"] = "NO"
df.loc[df.sample(70).index,"Savings Group Member"] = "YES"

# Saving CSV
df.to_csv("Women's_Socioeconomic_Survey_data.csv",index=False)

print(df.head())

print(df.shape)