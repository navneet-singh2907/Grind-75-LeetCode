# 076. Minimum Window Substring

## Approach: Sliding Window
We use a two-pointer sliding window approach combined with two hash maps to track character frequencies. By expanding the right pointer to find a valid window and then contracting the left pointer to minimize it, we achieve an optimal linear time solution.

## Complexity Analysis
- **Time Complexity:** $O(m + n)$ — Where $m$ and $n$ are the lengths of strings $s$ and $t$.
- **Space Complexity:** $O(m + n)$ — In the worst case, the hash maps store all unique characters from both strings.
