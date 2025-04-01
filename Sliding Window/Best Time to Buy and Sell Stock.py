class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            currentProfit = prices[i] - minPrice
            maxProfit = max(maxProfit, currentProfit)
            minPrice = min(minPrice, prices[i])
        
        return maxProfit

