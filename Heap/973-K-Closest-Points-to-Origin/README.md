# 973. K Closest Points to Origin

## Approach: Max-Heap
We use a Max-Heap of size `k` to keep track of the closest points. By storing negative distances, we leverage Python's `heapq` (min-heap) to act as a max-heap. This ensures that we only keep the `k` smallest distances.

## Complexity Analysis
- **Time Complexity:** $O(n \log k)$ — We iterate through all $n$ points, and each heap operation takes $\log k$ time.
- **Space Complexity:** $O(k)$ — To store the `k` points in the heap.
