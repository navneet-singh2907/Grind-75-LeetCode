# 322. Coin Change

## Approach: Bottom-Up Dynamic Programming
We use a 1D array to store the minimum number of coins needed for every amount up to the target. By solving smaller subproblems first, we can build the optimal solution for the final amount using the recurrence relation: `dp[i] = min(dp[i], 1 + dp[i - coin])`.

## Complexity Analysis
- **Time Complexity:** $O(amount \times n)$ — Where $n$ is the number of coin denominations.
- **Space Complexity:** $O(amount)$ — To store the DP table.
