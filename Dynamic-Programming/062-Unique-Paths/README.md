# 062. Unique Paths

## Approach: Dynamic Programming (Space-Optimized)
This problem follows the Pascal's Triangle logic. The number of ways to reach a cell is the sum of the ways to reach the cell above and the cell to the left. We optimize the space from $O(m \times n)$ to $O(n)$ by only maintaining the current and previous rows.

## Complexity Analysis
- **Time Complexity:** $O(m \cdot n)$ — We visit every cell in the grid once.
- **Space Complexity:** $O(n)$ — We only store a single row of values.
