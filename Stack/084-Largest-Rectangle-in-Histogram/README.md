# 084. Largest Rectangle in Histogram

## Approach: Monotonic Increasing Stack
We use a monotonic stack to store indices of the histogram bars. For each bar, we identify its left and right boundaries (the first bars to its left and right that are shorter than it). By maintaining a stack of increasing heights, we can calculate the potential area for each bar in a single $O(n)$ pass.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — Each bar is pushed and popped from the stack at most once.
- **Space Complexity:** $O(n)$ — In the worst case (ascending heights), the stack stores all indices.
