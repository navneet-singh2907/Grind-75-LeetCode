# 981. Time Based Key-Value Store

## Approach: Hash Map & Binary Search
We use a hash map to store keys, where each key points to a list of `[value, timestamp]` pairs. Because the problem guarantees timestamps are added in increasing order, we can use binary search to efficiently find the most recent value for a key that does not exceed a given timestamp.

## Complexity Analysis
- **Time Complexity:** - `set`: $O(1)$
  - `get`: $O(\log n)$ where $n$ is the number of values for a specific key.
- **Space Complexity:** $O(M \times N)$ — Where $M$ is the number of keys and $N$ is the number of values stored.
