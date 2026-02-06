# 278. First Bad Version

## Approach: Binary Search
Since we need to find the first occurrence of a "Bad" state in a sorted sequence of versions, Binary Search is the most efficient method. It reduces the search space by half in each step, allowing us to find the culprit version in logarithmic time.

## Complexity Analysis
- **Time Complexity:** $O(\log n)$ — The search space is halved at each iteration.
- **Space Complexity:** $O(1)$ — We only use two pointers.
