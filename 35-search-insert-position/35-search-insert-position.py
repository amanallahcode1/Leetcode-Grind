class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] == target:
                return mid
        
        for i in range(1, len(nums)):
            if target < nums[0]:
                return 0
            if target > nums[len(nums) - 1]:
                return len(nums)
            if target > nums[i-1] and target < nums[i]:
                return i
        if len(nums) == 1:
            if target < nums[0]:
                return 0
            else:
                return 1
                
            
        
        
           
            