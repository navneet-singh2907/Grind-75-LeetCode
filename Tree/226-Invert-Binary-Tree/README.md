# 226. Invert Binary Tree

## Approach: Recursion (DFS)
We use a recursive Depth-First Search (DFS) approach to traverse the tree. At each node, we perform a simple swap of its left and right pointers before moving deeper into the tree.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We visit every node exactly once.
- **Space Complexity:** $O(h)$ — Where $h$ is the height of the tree, representing the space used by the recursion stack.
