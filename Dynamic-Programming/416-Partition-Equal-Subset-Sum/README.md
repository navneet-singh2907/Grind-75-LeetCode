# 416. Partition Equal Subset Sum

## Approach: Dynamic Programming (Set-based 0/1 Knapsack)
The problem reduces to finding a subset that sums to exactly half of the total sum. We use a set to track all possible sums reachable by iterating through the numbers. This is a space-optimized version of the 0/1 Knapsack problem.

## Complexity Analysis
- **Time Complexity:** $O(n \cdot \text{target})$ — Where $n$ is the number of elements and `target` is half the total sum.
- **Space Complexity:** $O(\text{target})$ — To store the reachable sums in a set.
