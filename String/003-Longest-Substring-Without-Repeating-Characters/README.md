# 003. Longest Substring Without Repeating Characters

## Approach: Sliding Window (Optimized)
We use a sliding window defined by two pointers. A hash map stores the most recent index of each character. When a duplicate is encountered within the current window, we jump the left pointer to the position immediately following the last occurrence of that character.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We traverse the string once with the right pointer.
- **Space Complexity:** $O(min(m, n))$ — Where $m$ is the size of the character set (e.g., 26 for letters or 128 for ASCII).
