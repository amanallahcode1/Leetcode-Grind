class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # search right side
                l = m + 1
            else:
                # search left side
                r = m - 1
        return res