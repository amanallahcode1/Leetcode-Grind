class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # We are going to have 2 pointers, a left and right
        # Starts off at 0 and 1 
        
        # If prices[l] < prices[r]:
        # new_max = max(new_max, prices[r] - prices[l])
        # r+=1
        # else:
        # l = r
        
        l, r = 0, 1
        new_max = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                new_max = max(new_max, prices[r] - prices[l])
                r+=1
            else:
                l = r
                r+=1
        return new_max
                
        
        