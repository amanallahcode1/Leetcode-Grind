class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = float('inf')
        
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(nums[l], minimum)
                break
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                minimum = min(minimum, nums[m])
                l = m + 1
            else:
                minimum = min(minimum, nums[m])
                r = m - 1
        return minimum
        