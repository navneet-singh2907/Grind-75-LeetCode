Best Time to Buy and Sell Stock

## Approach: Sliding Window
Instead of comparing every possible pair of days ($O(n^2)$), we maintain a `min_buy` variable to track the lowest price encountered so far. For every new price, we calculate the potential profit and update `max_profit` if it's higher than our previous record.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We only iterate through the prices once.
- **Space Complexity:** $O(1)$ — We only store two variables, regardless of input size.
