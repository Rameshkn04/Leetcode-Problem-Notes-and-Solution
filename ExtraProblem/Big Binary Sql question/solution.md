We’ll solve this in two steps:

Aggregate posts per user (count + average likes)

Pick the top 3 users per location

✅ SQL Query
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

🧠 Explanation (easy to remember)

JOIN users u JOIN posts p → connect users with their posts

COUNT(p.post_id) → total posts per user

AVG(p.likes) → average likes per post

HAVING → filter users with:

at least 5 posts

avg likes > 100

ROW_NUMBER() OVER (PARTITION BY location) → rank users per location

WHERE rn <= 3 → get top 3 users per location

📌 Output Columns

username

location

total_posts

avg_likes

🔥 VTU / Interview Tip

If window functions are not allowed, you can mention:

“This can also be solved using correlated subqueries, but window functions are more efficient and readable.”
