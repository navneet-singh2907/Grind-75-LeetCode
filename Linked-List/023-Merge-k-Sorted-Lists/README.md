# 023. Merge k Sorted Lists

## Approach: Min-Heap (Priority Queue)
To merge $k$ sorted lists efficiently, we use a Min-Heap to keep track of the smallest current element across all lists. This ensures we always pick the correct next node in $O(\log k)$ time. This approach is highly efficient for large datasets as it only keeps $k$ elements in memory at any given time.

## Complexity Analysis
- **Time Complexity:** $O(N \log k)$ — Where $N$ is the total number of nodes and $k$ is the number of linked lists.
- **Space Complexity:** $O(k)$ — The heap stores at most one node from each of the $k$ lists.
