# 704. Binary Search

##  Approach: Iterative Two-Pointer
Binary search finds the position of a target value within a sorted array. By comparing the target value to the middle element of the array, we can eliminate half of the remaining search space in each step.

##  Complexity Analysis
- **Time Complexity:** $O(\log n)$ — Because we divide the search space by half each time.
- **Space Complexity:** $O(1)$ — We only use a few pointer variables.
