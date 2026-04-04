# 078. Subsets

## Approach: Backtracking
We use a recursive backtracking approach to generate the Power Set. By using a `start` index, we ensure that we only process elements appearing after the current element in the input array, which naturally avoids duplicate subsets. Since every node in the decision tree represents a unique subset, we add a copy of the current path to our results at every recursive call.

## Complexity Analysis
- **Time Complexity:** $O(n \cdot 2^n)$ — There are $2^n$ possible subsets, and each takes $O(n)$ to copy into the result list.
- **Space Complexity:** $O(n)$ — To store the current subset and the recursion stack.
