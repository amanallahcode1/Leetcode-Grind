class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       
        ans = []
        l, r = 0, len(nums) - 1
        
        while l <= r:
            left_num, right_num = abs(nums[l]), abs(nums[r])
            if right_num > left_num:
                ans.append(right_num ** 2)
                r -= 1
            else:
                ans.append(left_num ** 2)
                l += 1
        return ans[::-1]
            
      
            