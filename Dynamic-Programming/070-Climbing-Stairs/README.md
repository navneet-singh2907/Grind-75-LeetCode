# 070. Climbing Stairs

## Approach: Iterative Dynamic Programming (Fibonacci)
The number of ways to reach the $n$-th step is the sum of ways to reach the $(n-1)$-th and $(n-2)$-th steps. This follows the Fibonacci sequence pattern. We optimize the space complexity from $O(n)$ to $O(1)$ by only storing the previous two results.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We iterate through the steps once.
- **Space Complexity:** $O(1)$ — We only use three variables regardless of $n$.
