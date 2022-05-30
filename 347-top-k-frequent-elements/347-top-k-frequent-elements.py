from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket_arr = [[] for i in range(len(nums) + 1)]
        nums_counter = Counter(nums)
        
        for element, count in nums_counter.items():
            bucket_arr[count].append(element)
        
        for i in range(len(nums), 0, -1):
            for n in bucket_arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
            