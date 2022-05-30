import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minimum = math.inf
        windowStart = 0
        runningSum = 0
        
        for windowEnd in range(len(nums)):
            runningSum += nums[windowEnd]
            
            while runningSum >= target:
                minimum = min(minimum, windowEnd - windowStart + 1)
                runningSum -= nums[windowStart]
                windowStart += 1
        
        if minimum == math.inf:
            return 0
        else:
            return minimum
        