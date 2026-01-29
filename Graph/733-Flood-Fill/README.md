# 733. Flood Fill

## Approach: Depth-First Search (DFS)
We use a recursive DFS to visit all adjacent pixels that share the same starting color. By checking bounds and color matches at each step, we ensure we only fill the connected component.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — Where $n$ is the total number of pixels in the image.
- **Space Complexity:** $O(n)$ — In the worst case, the recursion stack could grow to the size of the image.
