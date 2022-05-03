class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = 0
                nums[index] = temp
                index += 1
        # Space -> O(1) & Time -> O(n)
        
        
            
        
        
        