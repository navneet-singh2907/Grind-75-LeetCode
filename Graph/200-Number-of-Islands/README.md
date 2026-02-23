# 200. Number of Islands

## Approach: Depth-First Search (DFS)
We iterate through the grid. When land ('1') is encountered, we increment the island count and trigger a DFS to "sink" all connected land pieces by changing them to '0'. This ensures each island is counted exactly once.

##  Complexity Analysis
- **Time Complexity:** $O(M \times N)$ — Every cell in the grid is visited at most once.
- **Space Complexity:** $O(M \times N)$ — In the worst case (the entire grid is land), the recursion stack can go up to $M \times N$.
