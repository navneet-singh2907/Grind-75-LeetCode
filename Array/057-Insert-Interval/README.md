# 057. Insert Interval

## Approach: Linear Scan
Since the input intervals are already sorted, we can iterate through them once. We categorize intervals into three groups: those that end before the new interval, those that overlap (and must be merged), and those that start after.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We process each interval exactly once.
- **Space Complexity:** $O(n)$ — To store the output list of intervals.
