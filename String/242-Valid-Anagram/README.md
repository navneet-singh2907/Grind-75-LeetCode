# 242. Valid Anagram

## Approach: Hash Map
We use a dictionary to track the frequency of each character. This is more efficient than sorting ($O(n \log n)$) because it only requires a single pass through the data.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — Linear time to traverse the strings.
- **Space Complexity:** $O(1)$ — The space is limited by the alphabet size (26 characters).
