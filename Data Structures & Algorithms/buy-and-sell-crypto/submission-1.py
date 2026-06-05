class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for buyDay, buyPrice in enumerate(prices):
            for saleDay, salePrice in enumerate(prices[min(buyDay+1, len(prices)-1):]):
                    maxProfit = max(maxProfit, salePrice - buyPrice)
        return maxProfit
