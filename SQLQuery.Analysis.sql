--County Economic Summary

--Business question: Which counties have higher average income and savings?

CREATE VIEW vw_CountySummary AS
SELECT
    County,
    COUNT(*) AS TotalParticipants,
    AVG([Monthly_Income]) AS AverageIncome,
    AVG([Monthly_Savings]) AS AverageSavings
FROM WSurvey
GROUP BY County;




--Education and Income

--Business question: Does education level influence income and savings?

CREATE VIEW vw_EducationSummary AS
SELECT
    [Education_Level],
    COUNT(*) AS TotalParticipants,
    AVG([Monthly_Income]) AS AverageIncome,
    AVG([Monthly_Savings]) AS AverageSavings
FROM WSurvey
GROUP BY [Education_Level];

--occuoation summary

CREATE VIEW vw_OccupationSummary AS
SELECT
    Occupation,
    COUNT(*) AS TotalParticipants,
    AVG([Monthly_Income]) AS AverageIncome,
    AVG([Monthly_Savings]) AS AverageSavings
FROM WSurvey
GROUP BY Occupation;

--training impact

CREATE VIEW vw_TrainingImpact AS
SELECT
    [Training_Received],
    COUNT(*) AS TotalParticipants,
    AVG([Monthly_Income]) AS AverageIncome,
    AVG([Monthly_Savings]) AS AverageSavings,
    AVG([Monthly_Health_Expenses]) AS AverageHealthExpense
FROM WSurvey
GROUP BY [Training_Received];
