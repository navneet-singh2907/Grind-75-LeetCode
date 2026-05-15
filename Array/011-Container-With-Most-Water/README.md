# 011. Container With Most Water

## Approach: Two-Pointer (Greedy)
We use two pointers at opposite ends of the array. At each step, we calculate the area and then move the pointer that points to the shorter line, as this is the only way to potentially find a larger area.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — Single pass through the array.
- **Space Complexity:** $O(1)$ — Only two pointers are used.
