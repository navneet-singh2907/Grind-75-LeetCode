# 054. Spiral Matrix

## Approach: Boundary-Based Traversal
We maintain four boundaries (`top`, `bottom`, `left`, `right`) and iterate in a spiral pattern. After completing each edge of the spiral, we contract the corresponding boundary. We include a check before the 'Left' and 'Up' traversals to ensure we haven't crossed boundaries mid-loop, which is critical for non-square matrices.

## Complexity Analysis
- **Time Complexity:** $O(m \cdot n)$ — Every element in the matrix is visited exactly once.
- **Space Complexity:** $O(1)$ — Excluding the output list, only a constant amount of extra space is used for the boundaries.
