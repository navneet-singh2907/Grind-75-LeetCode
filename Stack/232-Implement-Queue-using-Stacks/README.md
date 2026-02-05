# 232. Implement Queue using Stacks

## Approach: Two Stacks (Amortized O(1))
We maintain two stacks: `in_stack` for incoming elements and `out_stack` for outgoing elements. When a pop/peek occurs and `out_stack` is empty, we transfer all elements from `in_stack` to `out_stack`, effectively reversing their order to achieve FIFO behavior.

## Complexity Analysis
- **Time Complexity:** - Push: $O(1)$
    - Pop/Peek: Amortized $O(1)$ — Each element is pushed and popped exactly twice across all operations.
- **Space Complexity:** $O(n)$ — To store the elements in the stacks.
