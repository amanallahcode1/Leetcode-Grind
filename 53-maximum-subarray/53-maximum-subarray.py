class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(N) Solution
        
        max_val = nums[0]
        running_sum = 0
        for number in nums:
            # when negative:
            if running_sum < 0:
                running_sum = 0
            running_sum+=number
            max_val = max(max_val, running_sum)
        return max_val