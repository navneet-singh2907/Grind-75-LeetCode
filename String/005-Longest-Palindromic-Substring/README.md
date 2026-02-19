# 005. Longest Palindromic Substring

## Approach: Expand Around Center
Every character (for odd lengths) and every gap between characters (for even lengths) is a potential center for a palindrome. By expanding outward from each of these $2n-1$ centers, we can find the longest palindromic substring efficiently.

## Complexity Analysis
- **Time Complexity:** $O(n^2)$ — We expand from each center, and there are $O(n)$ centers.
- **Space Complexity:** $O(1)$ — We only store a few pointers and the result string.
