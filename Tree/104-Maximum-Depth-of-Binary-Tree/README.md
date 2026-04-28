# 104. Maximum Depth of Binary Tree

## Approach: Recursive DFS
We use a bottom-up recursive approach to find the height of the tree. By calculating the maximum depth of both the left and right subtrees and adding one for the current root, we can determine the longest path from the root to any leaf.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We visit every node in the tree exactly once.
- **Space Complexity:** $O(h)$ — Where $h$ is the height of the tree, representing the recursion stack. In the worst case (a skewed tree), this is $O(n)$.
