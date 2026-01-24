# 020. Valid Parentheses

## 📝 Problem Description
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

## 💡 Approach: Stack (LIFO)
To solve this efficiently, we use a **Stack**. The key idea is that every time we encounter a closing bracket, it must match the most recently opened bracket.

- **Step 1:** Create a hash map for bracket pairs.
- **Step 2:** Push opening brackets onto the stack.
- **Step 3:** For closing brackets, pop from the stack and verify the match.

## 📊 Complexity Analysis
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$
