# 208. Implement Trie (Prefix Tree)

## Approach: Prefix Tree (Trie)
We implement the Trie using a custom `TrieNode` class. Each node stores its children in a hash map for $O(1)$ access. This structure is highly efficient for prefix-based searches compared to a standard hash set.

## Complexity Analysis
- **Time Complexity:** - Insert: $O(L)$ where $L$ is word length.
  - Search/StartsWith: $O(L)$.
- **Space Complexity:** $O(N \times L)$ where $N$ is the number of words.
