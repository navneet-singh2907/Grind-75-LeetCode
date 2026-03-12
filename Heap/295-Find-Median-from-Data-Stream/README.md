# 295. Find Median from Data Stream

## Approach: Two Heaps
We maintain a Max-Heap for the smaller half of the data and a Min-Heap for the larger half. By keeping these heaps balanced, we can find the median in $O(1)$ time while adding new elements takes $O(\log n)$ time. This is much more efficient than re-sorting the list for every new element.

## Complexity Analysis
- **Time Complexity:** - `addNum`: $O(\log n)$
  - `findMedian`: $O(1)$
- **Space Complexity:** $O(n)$ — To store all elements in the stream.
