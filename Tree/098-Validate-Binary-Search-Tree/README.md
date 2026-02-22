# 098. Validate Binary Search Tree

##  Approach: Recursive Boundary Validation
A common pitfall is only checking a node against its immediate children. To properly validate a BST, we must ensure every node satisfies a range constraint $(min, max)$ inherited from its ancestors. We use a DFS approach to pass these boundaries down the tree.

##  Complexity Analysis
- **Time Complexity:** $O(n)$ — Every node is visited exactly once.
- **Space Complexity:** $O(h)$ — Where $h$ is the tree height, representing the recursion stack.
