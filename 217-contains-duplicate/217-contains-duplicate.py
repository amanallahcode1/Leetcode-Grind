from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        counter_nums = Counter(nums)
        for value in counter_nums.values():
            if value > 1:
                return True
        return False