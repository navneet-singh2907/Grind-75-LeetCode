Merge Two Sorted Lists

## Problem Description
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

## Approach: Iteration with Dummy Node
We use a **Dummy Node** to simplify the edge case of an empty initial list. By maintaining a `tail` pointer, we can build the new list by comparing the heads of `list1` and `list2`.

1. **Compare:** Look at the current values of both lists.
2. **Link:** Point the `tail.next` to the smaller value.
3. **Advance:** Move the pointer of the chosen list forward.
4. **Cleanup:** If one list is exhausted, append the remainder of the other list.



## Complexity Analysis
- **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the lengths of the lists.
- **Space Complexity:** $O(1)$ as we are re-using the existing nodes.

