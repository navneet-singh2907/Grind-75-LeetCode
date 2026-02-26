# 033. Search in Rotated Sorted Array

## Approach: Modified Binary Search
We utilize the property that in a rotated sorted array, at least one half of the search space remains sorted. By identifying which half is sorted at each step, we can determine if the target lies within that range or the other, maintaining $O(\log n)$ time complexity.

## Complexity Analysis
- **Time Complexity:** $O(\log n)$ — The search space is halved at each iteration.
- **Space Complexity:** $O(1)$ — Only a constant amount of extra space is used for pointers.
