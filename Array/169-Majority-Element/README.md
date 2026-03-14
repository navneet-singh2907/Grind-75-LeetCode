# 169. Majority Element

##  Approach: Boyer-Moore Voting Algorithm
Since the majority element is guaranteed to appear more than half the time, we can use a voting approach. We maintain a candidate and a count that increments on matches and decrements on mismatches. The majority element will always be the last candidate standing.

##  Complexity Analysis
- **Time Complexity:** $O(n)$ — We pass through the array exactly once.
- **Space Complexity:** $O(1)$ — We only store two variables, regardless of the input size.
