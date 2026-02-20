# 155. Min Stack

## Approach: Two Stacks
We maintain two stacks: a main stack for all values and a `min_stack` that stores the minimum value at each level of the main stack. This allows us to retrieve the minimum element in $O(1)$ time by always looking at the top of the `min_stack`.

## Complexity Analysis
- **Time Complexity:** $O(1)$ for all operations (Push, Pop, Top, GetMin).
- **Space Complexity:** $O(n)$ — We store twice the number of elements in the worst case.
