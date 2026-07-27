/*==========================================
03_FUNNEL_ANALYSIS.SQL
==========================================*/

-- ==========================================
-- 1. Users at Each Funnel Stage
-- ==========================================

SELECT
    event_type,
    COUNT(DISTINCT user_id) AS users
FROM events
WHERE event_type IN (
    'Sign Up',
    'Login',
    'Upload File',
    'Create Dashboard',
    'Upgrade Plan'
)
GROUP BY event_type
ORDER BY FIELD(
    event_type,
    'Sign Up',
    'Login',
    'Upload File',
    'Create Dashboard',
    'Upgrade Plan'
);


-- ==========================================
-- 2. Funnel Conversion Rate
-- ==========================================

SELECT

    COUNT(DISTINCT CASE WHEN event_type='Sign Up' THEN user_id END) AS signups,

    COUNT(DISTINCT CASE WHEN event_type='Login' THEN user_id END) AS logins,

    COUNT(DISTINCT CASE WHEN event_type='Upload File' THEN user_id END) AS uploads,

    COUNT(DISTINCT CASE WHEN event_type='Create Dashboard' THEN user_id END) AS dashboards,

    COUNT(DISTINCT CASE WHEN event_type='Upgrade Plan' THEN user_id END) AS upgrades,

    ROUND(
        COUNT(DISTINCT CASE WHEN event_type='Upgrade Plan' THEN user_id END)
        *100.0/
        COUNT(DISTINCT CASE WHEN event_type='Sign Up' THEN user_id END),
        2
    ) AS overall_conversion_rate

FROM events;


-- ==========================================
-- 3. Activation Rate
-- (Users who created at least one dashboard)
-- ==========================================

SELECT

    COUNT(DISTINCT user_id) AS total_users,

    (
        SELECT COUNT(DISTINCT user_id)
        FROM events
        WHERE event_type='Create Dashboard'
    ) AS activated_users,

    ROUND(

        (
            SELECT COUNT(DISTINCT user_id)
            FROM events
            WHERE event_type='Create Dashboard'
        )

        *100.0/

        COUNT(DISTINCT user_id),

        2

    ) AS activation_rate

FROM users;


-- ==========================================
-- 4. Plan Upgrade Analysis
-- ==========================================

SELECT

    plan_type,

    COUNT(*) AS users

FROM subscriptions

GROUP BY plan_type

ORDER BY FIELD(
    plan_type,
    'Free',
    'Basic',
    'Pro'
);