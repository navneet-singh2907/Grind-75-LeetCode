# 721. Accounts Merge

##  Approach: Union-Find (DSU)
This is an Entity Resolution problem. We treat each account as a node and use Union-Find to merge accounts that share a common email. By mapping emails to their respective account indices, we can efficiently find and unite connected components of emails belonging to the same person.

## Complexity Analysis
- **Time Complexity:** $O(NK \log NK)$ — Where $N$ is the number of accounts and $K$ is the max number of emails per account (due to sorting).
- **Space Complexity:** $O(NK)$ — To store the Union-Find structure and the email mappings.
