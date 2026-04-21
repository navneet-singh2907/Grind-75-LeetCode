# 1235. Maximum Profit in Job Scheduling

## Approach: DP + Binary Search
We solve this by sorting jobs based on their end times and using dynamic programming to track the maximum profit at each point. For each job, we use binary search to find the most recent job that does not overlap with the current one. This allows us to decide if including the current job yields a higher profit than the maximum profit recorded so far.

## Complexity Analysis
- **Time Complexity:** $O(n \log n)$ — Due to sorting the $n$ jobs and performing a binary search for each job.
- **Space Complexity:** $O(n)$ — To store the sorted jobs and the DP table.
