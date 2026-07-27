/*==========================================
01_USER_ANALYTICS.SQL
==========================================*/

-- 1. Total Users

SELECT COUNT(*) AS total_users
FROM users;


-- 2. Activation Rate

SELECT
    COUNT(*) AS total_users,
    SUM(CASE WHEN activation_date IS NOT NULL THEN 1 ELSE 0 END) AS activated_users,
    ROUND(
        SUM(CASE WHEN activation_date IS NOT NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS activation_rate
FROM users;


-- 3. Monthly User Signups

SELECT
    DATE_FORMAT(signup_date,'%Y-%m') AS signup_month,
    COUNT(*) AS new_users
FROM users
GROUP BY signup_month
ORDER BY signup_month;


-- 4. Users by Acquisition Channel

SELECT
    acquisition_channel,
    COUNT(*) AS users
FROM users
GROUP BY acquisition_channel
ORDER BY users DESC;


-- 5. Users by Device

SELECT
    device,
    COUNT(*) AS users
FROM users
GROUP BY device
ORDER BY users DESC;


-- 6. Users by Country

SELECT
    country,
    COUNT(*) AS users
FROM users
GROUP BY country
ORDER BY users DESC;


-- 7. Plan Distribution

SELECT
    plan_type,
    COUNT(*) AS users
FROM users
GROUP BY plan_type
ORDER BY users DESC;

-- 8. Experiment Groups

SELECT
    experiment_group,
    COUNT(*) AS total_users
FROM users
GROUP BY experiment_group;

-- 9. Cohort Distribution


SELECT

    cohort_month,

    COUNT(*) AS users

FROM users

GROUP BY cohort_month

ORDER BY cohort_month;