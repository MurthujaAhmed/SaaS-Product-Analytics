/*==========================================
06_COHORT_ANALYSIS.SQL
==========================================*/

-- ==========================================
-- 1. Users per Cohort
-- ==========================================

SELECT
    cohort_month,
    COUNT(*) AS users
FROM users
GROUP BY cohort_month
ORDER BY cohort_month;


-- ==========================================
-- 2. Monthly Active Users by Cohort
-- ==========================================

SELECT
    u.cohort_month,
    DATE_FORMAT(e.event_time,'%Y-%m') AS activity_month,
    COUNT(DISTINCT e.user_id) AS active_users
FROM users u
JOIN events e
ON u.user_id = e.user_id
GROUP BY
    u.cohort_month,
    activity_month
ORDER BY
    u.cohort_month,
    activity_month;


-- ==========================================
-- 3. Cohort Size
-- ==========================================

SELECT
    cohort_month,
    COUNT(DISTINCT user_id) AS cohort_size
FROM users
GROUP BY cohort_month
ORDER BY cohort_month;


-- ==========================================
-- 4. Cohort Retention Rate
-- ==========================================

SELECT
    u.cohort_month,
    DATE_FORMAT(e.event_time,'%Y-%m') AS activity_month,
    ROUND(
        COUNT(DISTINCT e.user_id) * 100.0 /
        COUNT(DISTINCT u.user_id),
        2
    ) AS retention_rate
FROM users u
JOIN events e
ON u.user_id = e.user_id
GROUP BY
    u.cohort_month,
    activity_month
ORDER BY
    u.cohort_month,
    activity_month;