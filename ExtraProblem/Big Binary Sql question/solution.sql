SELECT
    username,
    location,
    total_posts,
    avg_likes
FROM (
    SELECT
        u.username,
        u.location,
        COUNT(p.post_id) AS total_posts,
        AVG(p.likes) AS avg_likes,
        ROW_NUMBER() OVER (
            PARTITION BY u.location
            ORDER BY AVG(p.likes) DESC
        ) AS rn
    FROM users u
    JOIN posts p
        ON u.user_id = p.user_id
    GROUP BY u.user_id, u.username, u.location
    HAVING COUNT(p.post_id) >= 5
       AND AVG(p.likes) > 100
) ranked_users
WHERE rn <= 3;
