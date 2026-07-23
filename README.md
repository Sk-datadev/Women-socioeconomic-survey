
# Women Socioeconomic Survey Analysis

#Table of contents
- [Project Overview](#project-overview)
- [Project Objectives](#project_objectives)
- [Data Generation](#data-generation)
- [Data Cleaning & Transformation](#data-cleaning-&-transformation)
- [SQL Analysis](#sql-analysis)
- [Data Visualization](#data-visualization)
- [Tools Used](#tools-used)
- [Key Findings](#key-findings)
- [Recommendations](#recommendations)



###Project Overview

This project presents an end-to-end data analytics workflow on a simulated women's socioeconomic survey dataset containing 6,500+ records. The objective was to analyze socioeconomic factors such as education, employment, income, savings behavior, business activities, digital access, healthcare access, and training participation.

The project demonstrates the complete journey of a data analyst, from creating realistic data to transforming it into meaningful insights through visualization.

###Project Objectives
Analyze the demographic characteristics of the survey participants.
Examine the relationship between education level and monthly income.
Assess employment and business ownership among participants.
Evaluate savings behavior and participation in savings groups.
Identify the most common business activities and challenges.
Assess access to smartphones, internet, and health insurance.
Generate insights to support data-driven decision-making.

<img width="592" height="335" alt="Dashboard_page1" src="https://github.com/user-attachments/assets/b0123aa9-875d-4a79-80af-7150bd378645" />

<img width="572" height="322" alt="DashBoard_page2" src="https://github.com/user-attachments/assets/f3f92486-70e0-4031-a7b7-8de8d3ffbae2" />



### Data Generation

 realistic synthetic dataset was created using **Python (NumPy and Pandas)**.

The dataset was designed to represent real-world socioeconomic conditions by including variables such as:
- Age
- County
- Marital status
- Education level
- Occupation
- Monthly income
- Savings
- Business ownership
- Business challenges
- Digital access
- Health insurance
- Training participation

To simulate real-world data challenges, the generated dataset was intentionally made messy by introducing:
- Missing values
- Duplicate records
- Inconsistent text formatting
- Extra spaces
- Mixed capitalization errors

---
### Data Cleaning & Transformation

The messy dataset was cleaned and prepared using **Python with Pandas and NumPy**.

Cleaning processes included:
- Handling missing values
- Removing duplicate records
- Standardizing inconsistent categorical values
- Correcting formatting issues
- Preparing clean data for analysis

---

### SQL Analysis

After cleaning, the dataset was loaded into SQL for further analysis.

SQL was used to:
- Explore relationships within the data
- Create analytical views
- Organize data for reporting
- Prepare summarized datasets for visualization

---

### Data Visualization

The final cleaned and transformed data was visualized using **Microsoft Power BI**.

An interactive dashboard was created to analyze:
- Demographic characteristics
- Income distribution
- Education and employment patterns
- Business activities and challenges
- Savings behavior
- Digital and healthcare access

---

### Tools Used

- Python (Pandas, NumPy)
- SQL (Queries, Views)
- Microsoft Power BI
- GitHub

---

### Key Skills Demonstrated

- Data Generation
- Data Cleaning
- Data Transformation
- SQL Analysis
- Dashboard Development
- Insight Generation
  
### Key Findings
Higher education is associated with higher income.
Farming is the most common business activity.
Savings remain low compared to income.
Lack of capital is the main business challenge.
Digital access improves with income.
Health insurance coverage is relatively low.
Most participants have not received formal training.

### Recommendations
Expand entrepreneurship support through access to affordable financing and business development programs.
Increase vocational and financial literacy training to improve income and savings outcomes.
Promote digital inclusion by improving access to smartphones, internet services, and digital skills.
Strengthen savings and financial inclusion initiatives by encouraging participation in savings groups and access to financial services.

This project demonstrates the complete data analytics pipeline, from raw data creation to actionable insights.
