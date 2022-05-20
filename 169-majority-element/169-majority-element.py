class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element, i = 0, 0
        for n in nums:
            if i == 0:
                element = n
            if element == n:
                i += 1
            else:
                i -= 1
        return element