# 056. Merge Intervals

## Approach: Sorting and Linear Scan
By sorting the intervals by their start times, we can resolve all overlaps in a single linear pass. For each interval, we check if it overlaps with the last added interval in our result list. If it does, we merge them; otherwise, we add it as a new interval.

## Complexity Analysis
- **Time Complexity:** $O(n \log n)$ — Due to the initial sorting of the intervals.
- **Space Complexity:** $O(\log n)$ or $O(n)$ — Depending on the space used by the sorting algorithm.
