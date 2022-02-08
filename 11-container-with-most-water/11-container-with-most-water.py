class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxRes = float('-inf')
        
        while l <= r:
            if height[l] > height[r]:
                maxRes = max(maxRes, height[r] * (r - l))
                r -=1
            else:
                maxRes = max(maxRes, height[l] * (r-l))
                l += 1
        return maxRes