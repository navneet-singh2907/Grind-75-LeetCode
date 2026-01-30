# 236. Lowest Common Ancestor of a Binary Tree

## Approach: Recursive DFS
We traverse the tree using Depth-First Search. A node is the LCA if:
1. One target (p or q) is in the left subtree and the other is in the right subtree.
2. The node itself is p or q, and the other target is in one of its subtrees.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We may need to visit all nodes in the worst case.
- **Space Complexity:** $O(h)$ — Where $h$ is the height of the tree (recursion stack).
