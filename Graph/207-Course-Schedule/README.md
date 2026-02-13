# 207. Course Schedule

## Approach: DFS Cycle Detection
We represent the courses as a directed graph and use Depth-First Search to detect cycles. A cycle exists if we encounter a node that is already in the current recursion stack (the `visiting_set`). If no cycles are found, it is a Directed Acyclic Graph (DAG), and the courses can be completed.

## Complexity Analysis
- **Time Complexity:** $O(V + E)$ — We visit every vertex (course) and every edge (prerequisite) once.
- **Space Complexity:** $O(V + E)$ — To store the adjacency list and the recursion stack.
