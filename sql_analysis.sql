-- 1. Total Customers vs Total Churned Customers
SELECT 
    COUNT(CustomerID) AS Total_Customers,
    SUM(Predicted_Churn) AS Total_Predicted_Churn,
    ROUND((SUM(Predicted_Churn) * 100.0 / COUNT(CustomerID)), 2) AS Churn_Rate_Percentage
FROM final_churn_predictions;

-- 2. Churn Rate by Subscription Type
SELECT 
    Subscription_Type,
    COUNT(CustomerID) AS Total_Users,
    SUM(Predicted_Churn) AS Churned_Users,
    ROUND(AVG(Churn_Probability) * 100, 2) AS Avg_Churn_Risk_Pct
FROM final_churn_predictions
GROUP BY Subscription_Type
ORDER BY Churned_Users DESC;

-- 3. High Risk Customers for Targeted Retention (Probability > 70%)
SELECT 
    CustomerID,
    Contract_Length,
    Total_Spend,
    Churn_Probability
FROM final_churn_predictions
WHERE Churn_Probability > 0.70
ORDER BY Churn_Probability DESC;