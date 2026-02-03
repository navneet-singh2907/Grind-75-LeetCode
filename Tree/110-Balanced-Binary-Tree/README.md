# 110. Balanced Binary Tree

## Approach: Bottom-Up Depth-First Search
We use recursion to determine the height of subtrees. To optimize, we check balance conditions while traversing. If any subtree is unbalanced, we "short-circuit" by returning -1, avoiding unnecessary calculations.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — Each node is visited once in a single post-order traversal.
- **Space Complexity:** $O(h)$ — Where $h$ is the height of the tree (recursion stack).
