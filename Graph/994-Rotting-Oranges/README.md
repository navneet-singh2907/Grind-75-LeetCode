# 994. Rotting Oranges

## Approach: Multi-Source BFS
This problem requires finding the shortest time for a process to complete across a grid, which is a classic BFS application. We use a queue to track all rotten oranges and spread the 'rot' minute by minute to adjacent fresh oranges until no more spreading is possible.

## Complexity Analysis
- **Time Complexity:** $O(M \times N)$ — We visit each cell in the grid a constant number of times.
- **Space Complexity:** $O(M \times N)$ — In the worst case, the queue could store a significant portion of the grid's oranges.
