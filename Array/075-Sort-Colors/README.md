# 075. Sort Colors

## Approach: Dutch National Flag Algorithm
We use a three-pointer approach to sort the array in a single pass ($O(n)$ time) and with constant space ($O(1)$). By maintaining boundaries for 0s at the beginning and 2s at the end, we effectively "push" the middle values (1s) into place as we iterate through the list.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We traverse the array exactly once.
- **Space Complexity:** $O(1)$ — The sort is performed in-place with no extra data structures.
