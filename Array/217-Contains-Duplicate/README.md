# 217. Contains Duplicate

## Approach: Hash Set
We utilize a hash set to track the elements we have encountered while traversing the array. Since set lookups and insertions take $O(1)$ on average, this allows us to determine if a duplicate exists in a single linear pass.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We iterate through the array once.
- **Space Complexity:** $O(n)$ — In the worst case (no duplicates), the set will store all $n$ elements.
