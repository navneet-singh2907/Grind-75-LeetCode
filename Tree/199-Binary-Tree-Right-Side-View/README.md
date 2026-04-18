# 199. Binary Tree Right Side View

## Approach: Breadth-First Search (BFS)
We perform a level-order traversal of the tree. Since we want the 'right side view', we capture the value of the last node at each level. By processing nodes level by level using a queue, we can easily identify the rightmost element before moving to the next depth.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We visit every node in the tree exactly once.
- **Space Complexity:** $O(d)$ — Where $d$ is the diameter of the tree, representing the maximum number of nodes stored in the queue at any level.
