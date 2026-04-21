# 224. Basic Calculator

## Approach: Stack-Based Evaluation
We evaluate the expression using a stack to manage nested levels (parentheses). We maintain a running total and a sign. When encountering an open parenthesis, we preserve the current state on the stack and reset. Upon closing, we apply the saved sign and add the saved result to the value computed within the brackets.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — Each character in the string is visited once.
- **Space Complexity:** $O(n)$ — In the worst case (deeply nested parentheses), the stack stores $n$ elements.
