/*==========================================
02_PRODUCT_ENGAGEMENT.SQL
==========================================*/

-- 1. Daily Active Users (DAU)

SELECT
    DATE(event_time) AS event_date,
    COUNT(DISTINCT user_id) AS dau
FROM events
GROUP BY DATE(event_time)
ORDER BY event_date;


-- 2. Weekly Active Users (WAU)

SELECT
    YEAR(event_time) AS year,
    WEEK(event_time) AS week,
    COUNT(DISTINCT user_id) AS wau
FROM events
GROUP BY YEAR(event_time), WEEK(event_time)
ORDER BY year, week;


-- 3. Monthly Active Users (MAU)

SELECT
    DATE_FORMAT(event_time,'%Y-%m') AS month,
    COUNT(DISTINCT user_id) AS mau
FROM events
GROUP BY month
ORDER BY month;


-- 4. Stickiness (DAU / MAU)

SELECT
    d.event_date,
    d.dau,
    m.mau,
    ROUND((d.dau / m.mau) * 100,2) AS stickiness_percentage
FROM
(
    SELECT
        DATE(event_time) AS event_date,
        COUNT(DISTINCT user_id) AS dau
    FROM events
    GROUP BY DATE(event_time)
) d
JOIN
(
    SELECT
        DATE_FORMAT(event_time,'%Y-%m') AS month,
        COUNT(DISTINCT user_id) AS mau
    FROM events
    GROUP BY month
) m
ON DATE_FORMAT(d.event_date,'%Y-%m') = m.month;


-- 5. Event Distribution

SELECT
    event_type,
    COUNT(*) AS total_events
FROM events
GROUP BY event_type
ORDER BY total_events DESC;


-- 6. Feature Adoption

SELECT
    feature_name,
    COUNT(*) AS total_usage
FROM events
GROUP BY feature_name
ORDER BY total_usage DESC;


-- 7. Core Feature Usage

SELECT
    is_core_feature,
    COUNT(*) AS total_events
FROM events
GROUP BY is_core_feature;