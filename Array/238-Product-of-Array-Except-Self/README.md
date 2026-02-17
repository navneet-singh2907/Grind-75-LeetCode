# 238. Product of Array Except Self

## Approach: Prefix and Suffix Products
To solve this in $O(n)$ without division, we calculate the prefix products (all elements to the left) and suffix products (all elements to the right) for each index. By multiplying these two values, we get the product of all elements except the current one.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We traverse the array twice.
- **Space Complexity:** $O(1)$ — Excluding the output array, we only use two variables (`prefix` and `suffix`).
