# 133. Clone Graph

## Approach: Depth-First Search (DFS) with Hash Map
To create a deep copy of a graph, we must handle cycles and multiple edges to the same node. We use a hash map to store the mapping from original nodes to their corresponding clones. If we encounter a node already in the map, we simply return its clone to prevent infinite recursion.

## Complexity Analysis
- **Time Complexity:** $O(V + E)$ — Where $V$ is the number of vertices and $E$ is the number of edges. We visit each node and each edge once.
- **Space Complexity:** $O(V)$ — To store the mapping in our hash map and the recursion stack.
