class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0
        l = 0
        
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxp = max(prices[r] - prices[l], maxp)
        return maxp
