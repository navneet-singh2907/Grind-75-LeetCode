# 876. Middle of the Linked List

## Approach: Tortoise and Hare (Two Pointers)
We use two pointers, `slow` and `fast`, both starting at the head. By moving `fast` at twice the speed of `slow`, we ensure that when `fast` reaches the end of the list, `slow` is positioned at the midpoint. This allows us to find the middle in $O(n)$ time with only a single pass.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We traverse the list once.
- **Space Complexity:** $O(1)$ — We only use two pointer variables.
