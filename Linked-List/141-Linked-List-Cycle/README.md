# 141. Linked List Cycle

## Approach: Floyd's Tortoise and Hare
We use two pointers moving at different speeds. If a cycle exists, the fast pointer will eventually "lap" the slow pointer within the cycle. If no cycle exists, the fast pointer will reach the end of the list.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — In the worst case, we visit each node.
- **Space Complexity:** $O(1)$ — We only use two pointers regardless of list size.
