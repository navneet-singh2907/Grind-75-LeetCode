# 008. String to Integer (atoi)

## Approach: Linear Parsing
We simulate the parsing logic of the standard `atoi` function. By handling whitespace, signs, and digit conversion in a specific order, we ensure the string is correctly transformed. The final result is clamped to the 32-bit signed integer range to prevent overflow.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We traverse the string once.
- **Space Complexity:** $O(1)$ — We use a constant amount of extra space for variables.
