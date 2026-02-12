# 150. Evaluate Reverse Polish Notation

## Approach: Stack (Postfix Evaluation)
We use a stack to store operands. When an operator is encountered, we pop the top two elements, perform the operation, and push the result back. This ensures the correct order of operations without needing parentheses.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We iterate through the tokens once.
- **Space Complexity:** $O(n)$ — In the worst case, the stack stores all numbers in the expression.
