class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price - low > max_profit:
                max_profit = max(max_profit, price-low)
            low = min(low, price)
        return max_profit
            
        
        