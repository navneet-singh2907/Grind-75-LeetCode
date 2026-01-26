Valid Palindrome

## Approach: Two Pointers
Instead of creating a new filtered string, we use two pointers to compare characters from the outside in. This allows us to ignore non-alphanumeric characters on the fly.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — Each character is visited at most once.
- **Space Complexity:** $O(1)$ — No extra data structures are used.
