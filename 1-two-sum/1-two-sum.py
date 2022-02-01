class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # So we're going to use a hash map
        # Add all nums in nums list to hash map with key as the number and value as index
        # Then run another iteration:
        # If the complement which is (target - nums[i]) is in the hashmap and hashmap[complement] != i:
        
           # return i and hashmap[complement]
        hash_map = {}    
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map and hash_map[complement] != i:
                return [hash_map[complement], i]
                