class Solution:
    def maxProfit(self, prices):
        min_buy = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_buy:
                min_buy = price
            else:
                max_profit = max(max_profit, price - min_buy)
                
        return max_profit
