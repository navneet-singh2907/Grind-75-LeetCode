# 139. Word Break

##  Approach: Dynamic Programming (Bottom-Up)
We use a 1D DP array where `dp[i]` represents whether the prefix `s[0...i-1]` can be segmented into dictionary words. For each position `i`, we look back at all previous positions `j`. If `dp[j]` is true and the substring `s[j...i-1]` exists in the dictionary, then `dp[i]` is marked true.

##  Complexity Analysis
- **Time Complexity:** $O(n^2 \cdot k)$ — Where $n$ is the length of the string and $k$ is the average length of words in the dictionary (for string slicing/hashing).
- **Space Complexity:** $O(n)$ — To store the DP table.
