# 417. Pacific Atlantic Water Flow

## Approach: Multi-Source DFS
Instead of checking where water flows down, we check where it can flow "up" from the ocean edges. We maintain two sets (Pacific and Atlantic) and perform DFS starting from the respective borders. The intersection of these sets provides the coordinates that can reach both oceans.

## Complexity Analysis
- **Time Complexity:** $O(m \times n)$ — Each cell is visited at most twice (once for each ocean).
- **Space Complexity:** $O(m \times n)$ — To store the sets of visited cells and the recursion stack.
