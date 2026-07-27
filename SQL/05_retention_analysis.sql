/*==========================================
04_RETENTION_ANALYSIS.SQL
==========================================*/

-- ==========================================
-- 1. Active vs Cancelled Users
-- ==========================================

SELECT
    status,
    COUNT(*) AS users
FROM subscriptions
GROUP BY status;


-- ==========================================
-- 2. Churn Rate
-- ==========================================

SELECT
    COUNT(*) AS total_users,
    SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END) AS churned_users,
    ROUND(
        SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END)
        *100.0/COUNT(*),
        2
    ) AS churn_rate
FROM subscriptions;


-- ==========================================
-- 3. Monthly Active Users (Returning Users)
-- ==========================================

SELECT
    DATE_FORMAT(event_time,'%Y-%m') AS month,
    COUNT(DISTINCT user_id) AS active_users
FROM events
GROUP BY month
ORDER BY month;


-- ==========================================
-- 4. Renewal Analysis
-- ==========================================

SELECT
    plan_type,
    AVG(renewal_count) AS avg_renewals
FROM subscriptions
GROUP BY plan_type
ORDER BY avg_renewals DESC;