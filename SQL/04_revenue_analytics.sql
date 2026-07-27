/*==========================================
05_REVENUE_ANALYSIS.SQL
==========================================*/

-- ==========================================
-- 1. Monthly Recurring Revenue (MRR)
-- ==========================================

SELECT
    DATE_FORMAT(payment_date, '%Y-%m') AS month,
    SUM(amount) AS monthly_revenue
FROM payments
WHERE payment_status = 'Success'
GROUP BY month
ORDER BY month;


-- ==========================================
-- 2. Revenue by Subscription Plan
-- ==========================================

SELECT
    s.plan_type,
    SUM(p.amount) AS total_revenue
FROM payments p
JOIN subscriptions s
ON p.subscription_id = s.subscription_id
WHERE p.payment_status = 'Success'
GROUP BY s.plan_type
ORDER BY total_revenue DESC;


-- ==========================================
-- 3. Average Revenue Per User (ARPU)
-- ==========================================

SELECT
    ROUND(
        SUM(amount) /
        COUNT(DISTINCT user_id),
        2
    ) AS arpu
FROM payments
WHERE payment_status = 'Success';


-- ==========================================
-- 4. Payment Success Rate
-- ==========================================

SELECT
    payment_status,
    COUNT(*) AS total_payments,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM payments),
        2
    ) AS percentage
FROM payments
GROUP BY payment_status;
