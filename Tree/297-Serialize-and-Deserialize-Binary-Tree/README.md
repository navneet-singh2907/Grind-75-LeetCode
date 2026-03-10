# 297. Serialize and Deserialize Binary Tree

## Approach: DFS Pre-order Traversal
We use a Depth-First Search (Pre-order) to convert the tree into a comma-separated string. By explicitly marking `None` nodes with a placeholder (e.g., 'N'), we preserve the structure of the tree. Deserialization reverses this by consuming the string tokens to rebuild nodes recursively.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We visit every node once during both serialization and deserialization.
- **Space Complexity:** $O(n)$ — To store the serialized string and the recursion stack.
