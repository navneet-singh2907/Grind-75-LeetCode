# 542. 01 Matrix

## Approach: Multi-Source BFS
We treat all `0` cells as starting points for a Breadth-First Search. By processing cells level-by-level, we guarantee that the first time we reach a `1`, we have found its shortest distance to a `0`.

## Complexity Analysis
- **Time Complexity:** $O(m \times n)$ — We visit each cell at most once.
- **Space Complexity:** $O(m \times n)$ — In the worst case, the queue stores all cells.
