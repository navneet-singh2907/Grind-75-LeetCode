# 102. Binary Tree Level Order Traversal

##  Approach: Breadth-First Search (BFS)
We use a queue to traverse the tree level by level. By recording the queue size at the start of each level's iteration, we can process all nodes belonging to the same depth together before moving on to their children.

##  Complexity Analysis
- **Time Complexity:** $O(n)$ — Every node in the tree is visited exactly once.
- **Space Complexity:** $O(n)$ — In the worst case (a perfect binary tree), the queue will hold up to $n/2$ nodes at the lowest level.
