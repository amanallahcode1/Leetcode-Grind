class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            values[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in values and i != values[complement]:
                return [i, values[complement]]
        