This is a classic Dynamic Programming problem (often called Post Office / Mailbox Allocation).
I’ll explain the idea clearly and then give you a working solution approach you can use in exams or coding rounds.

🧠 Key Insight

Houses are on a 1D line (x-coordinates).

To minimize total distance, each postbox should be placed at the median of the houses it serves.

We must divide the houses into k groups, and each group gets 1 postbox.

Goal: minimize the sum of distances from houses to their nearest postbox.

Step 1: Sort the house positions

(This is required for median-based optimization.)

Step 2: Precompute cost for placing 1 postbox for any range

Let
cost[i][j] = minimum distance if one postbox serves houses from index i to j.

➡️ The best place is the median house.

median = (i + j) / 2
cost = Σ |houses[t] - houses[median]|  for t = i to j

Step 3: Dynamic Programming

Let
dp[m][i] = minimum distance to serve first i houses using m postboxes.

Transition:
dp[m][i] = min over x < i of:
           dp[m-1][x] + cost[x][i-1]

Base Case:
dp[0][0] = 0
dp[0][i>0] = infinity

✅ Final Answer

dp[k][n] where n is number of houses.
