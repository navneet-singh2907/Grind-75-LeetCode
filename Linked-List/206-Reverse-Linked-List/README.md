# 206. Reverse Linked List

## Approach: Iterative Pointer Manipulation
We use an iterative approach with three pointers (`prev`, `curr`, `nxt`) to reverse the direction of the `next` pointers in a single pass. This allows us to reverse the list in-place without using extra space.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We visit each node exactly once.
- **Space Complexity:** $O(1)$ — We only use a constant amount of extra space for pointers.
