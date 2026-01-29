A social media company, "ConnectMe", wants to analyze the user engagement on its platform. The company has two tables, users and posts, in its database. The users table has the following columns: user_id (primary key), username, and location. The posts table has the following columns: post_id (primary key), user_id (foreign key referencing the users table), and likes.

The company wants to find the top 3 users who have posted at least 5 times and have an average of more than 100 likes per post, grouping them by location. The result should include the username, location, total posts, and average likes per post.

Write a SQL query to solve this problem.
