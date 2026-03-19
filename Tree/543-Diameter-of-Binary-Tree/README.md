# 543. Diameter of Binary Tree

## Approach: Recursive Depth-First Search
We calculate the diameter by finding the maximum depth of the left and right subtrees for every node. The diameter passing through a node is the sum of these two depths. By maintaining a global `max_diameter` variable, we can capture the longest path even if it doesn't pass through the root of the tree.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We visit every node exactly once.
- **Space Complexity:** $O(h)$ — Where $h$ is the height of the tree, representing the recursion stack.
