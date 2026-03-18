# 067. Add Binary

## Approach: Iterative Bit Addition
We simulate the process of manual binary addition by iterating from the rightmost bit to the left. By maintaining a `carry` variable and using modular arithmetic (`total % 2`) for the digit and floor division (`total // 2`) for the carry, we ensure the logic holds for all binary combinations.

## Complexity Analysis
- **Time Complexity:** $O(\max(N, M))$ — Where $N$ and $M$ are lengths of strings `a` and `b`.
- **Space Complexity:** $O(\max(N, M))$ — To store the result string.
