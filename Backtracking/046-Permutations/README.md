# 046. Permutations

## Approach: Backtracking
We use a recursive backtracking approach to generate all possible orderings. By maintaining a `used` set, we ensure each number is only included once per permutation. The algorithm explores every possible path in the decision tree, capturing a snapshot of the path once its length matches the input array.

## Complexity Analysis
- **Time Complexity:** $O(n \cdot n!)$ — There are $n!$ permutations, and each takes $O(n)$ to copy into the result.
- **Space Complexity:** $O(n!)$ — To store all possible permutations.
