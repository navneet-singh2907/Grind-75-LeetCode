# 015. 3Sum

## Approach: Sorting + Two Pointers
To find unique triplets that sum to zero, we sort the input array and iterate through it. For each element, we use a two-pointer approach to find the remaining two numbers. Sorting is crucial as it allows us to handle duplicates efficiently by skipping identical adjacent values.

## Complexity Analysis
- **Time Complexity:** $O(n^2)$ — Sorting takes $O(n \log n)$, and the nested loops for the fixed pointer and two pointers take $O(n^2)$.
- **Space Complexity:** $O(1)$ or $O(n)$ — Depending on the sorting implementation's space requirements.
