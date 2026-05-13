# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Approach: Recursive Divide and Conquer
We leverage the properties of tree traversals: the first element of `preorder` is the root, and this root splits the `inorder` array into left and right subtrees. By using a hash map to quickly locate the root's index in the inorder array, we can reconstruct the tree in linear time.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We process each node exactly once.
- **Space Complexity:** $O(n)$ — To store the hash map and the recursion stack.
