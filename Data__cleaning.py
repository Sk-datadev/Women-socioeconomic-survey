import pandas as pd
import numpy as np

df = pd.read_csv("Women's_Socioeconomic_Survey_data.csv")


#checking nulls
#print(df.isnull().sum().sum()) #7346 nulls found

#checking duplicates
#print(df.duplicated().sum()) # 90 duplicates found
#removing duplicates
df = df.drop_duplicates()

##removing extra spaces
df["County"] = df["County"].str.strip()
df["Marital Status"] = df["Marital Status"].str.strip()
df["Education Level"] = df["Education Level"].str.strip()
df["Occupation"] = df["Occupation"].str.strip()
df["Savings Group Member"] = df["Savings Group Member"].str.strip()
df["Owns Business"] = df["Owns Business"].str.strip()
df["Business Type"] = df["Business Type"].str.strip()
df["Main Business Challenge"] = df["Main Business Challenge"].str.strip()
df["Smartphone Access"] = df["Smartphone Access"].str.strip()
df["Internet Access"] = df["Internet Access"].str.strip()
df["Health Insurance"] = df["Health Insurance"].str.strip()
df["Training Received"] = df["Training Received"].str.strip()


##handling missing values (solution depends on the column)
 #For numeric columns (Age, Monthly Income, Monthly Savings), filling  missing values with the median.
df["Age"] = df["Age"].fillna(df["Age"].median())

df["Monthly Income"] = df["Monthly Income"].fillna(df["Monthly Income"].median())

df["Monthly Savings"] = df["Monthly Savings"].fillna(df["Monthly Savings"].median())

df["Number of Dependents"] = df["Number of Dependents"].fillna(df["Number of Dependents"].median())

df["Monthly Health Expenses"] = df["Monthly Health Expenses"].fillna(df["Monthly Health Expenses"].median())

df["Caregiving in hours/Week"] = df["Caregiving in hours/Week"].fillna(df["Caregiving in hours/Week"].median())

 #For text columns, using the mode (the most common value).

    #finds the most common county.(mode)
    #picks the first (most common) value returned.
    #replaces every missing county with that value.
    #saves the updated column.

df["County"] = df["County"].fillna(df["County"].mode()[0])
df["Marital Status"] = df["Marital Status"].fillna(df["Marital Status"].mode()[0])
df["Education Level"] = df["Education Level"].fillna(df["Education Level"].mode()[0])
df["Occupation"] = df["Occupation"].fillna(df["Occupation"].mode()[0])
df["Savings Group Member"] = df["Savings Group Member"].fillna(df["Savings Group Member"].mode()[0])
df["Owns Business"] = df["Owns Business"].fillna(df["Owns Business"].mode()[0])
df["Business Type"] = df["Business Type"].fillna(df["Business Type"].mode()[0])
df["Main Business Challenge"] = df["Main Business Challenge"].fillna(df["Main Business Challenge"].mode()[0])
df["Smartphone Access"] = df["Smartphone Access"].fillna(df["Smartphone Access"].mode()[0])
df["Internet Access"] = df["Internet Access"].fillna(df["Internet Access"].mode()[0])
df["Health Insurance"] = df["Health Insurance"].fillna(df["Health Insurance"].mode()[0])
df["Training Received"] = df["Training Received"].fillna(df["Training Received"].mode()[0])

##standard capitalization(yes or no)
df["Health Insurance"] = df["Health Insurance"].str.title()

df["Training Received"] = df["Training Received"].str.title()

df["Savings Group Member"] = df["Savings Group Member"].str.title()

#deleting rows with null id
df = df.dropna(subset=["Participant ID"])
##verify data types
#df.dtypes

#changing the data type
int_columns = [
    "Participant ID",
    "Age",
    "Monthly Income",
    "Monthly Savings",
    "Number of Dependents",
    "Monthly Health Expenses",
    "Caregiving in hours/Week"
]

df[int_columns] = df[int_columns].astype(int)
print(df.head())


df.to_csv("Women's_Socioeconomic_Survey_data_clean.csv", index=False)