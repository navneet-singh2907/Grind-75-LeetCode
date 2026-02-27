# 039. Combination Sum

## Approach: Backtracking (DFS)
We use a recursive backtracking approach to explore all possible combinations. By branching into two decisions at each step—either including the current candidate or skipping it—we ensure all potential paths are explored while maintaining uniqueness in our results.

## Complexity Analysis
- **Time Complexity:** $O(2^t)$ — Where $t$ is the target value. The number of recursive calls can grow exponentially.
- **Space Complexity:** $O(t/min\_val)$ — The depth of the recursion stack.
