# 053. Maximum Subarray

## Approach: Kadane's Algorithm (Greedy)
We iterate through the array once, maintaining a `current_sum`. If `current_sum` drops below zero, we reset it to zero because a negative sum will only decrease the potential total of any future subarray. We track the `max_sum` throughout the process.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We iterate through the array exactly once.
- **Space Complexity:** $O(1)$ — We only use two variables for tracking.
