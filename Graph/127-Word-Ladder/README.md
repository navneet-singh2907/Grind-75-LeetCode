# 127. Word Ladder

## Approach: BFS with Pattern Pre-processing
To find the shortest transformation sequence, BFS is the optimal choice. We optimize the search by pre-processing the `wordList` into a dictionary of generic patterns. This allows us to find all "one-letter-off" neighbors in $O(L)$ time rather than $O(N)$, significantly speeding up the traversal.

## Complexity Analysis
- **Time Complexity:** $O(M^2 \cdot N)$ — Where $M$ is the length of each word and $N$ is the total number of words in the dictionary.
- **Space Complexity:** $O(M^2 \cdot N)$ — To store the pattern dictionary and the BFS queue.
