class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum = float('-inf')
        count = 0
        
        for i in nums:
            count += i
            if count > maximum:
                maximum = count
            if count < 0:
                count = 0
        return maximum
        
#         Initialize:
#     max_so_far = INT_MIN
#     max_ending_here = 0

# Loop for each element of the array
#   (a) max_ending_here = max_ending_here + a[i]
#   (b) if(max_so_far < max_ending_here)
#             max_so_far = max_ending_here
#   (c) if(max_ending_here < 0)
#             max_ending_here = 0
# return max_so_far
        
    
        