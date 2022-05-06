class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        forward = 1
        
        for i in range(len(prices) - 1):
            current = prices[forward] - prices[i]
            if current > 0:
                total += current
            forward += 1
        return total