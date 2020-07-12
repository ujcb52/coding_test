from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
    
#        d = {}
#        for i, n in enumerate(nums):
#            m = target - n
#            if m in d:
#                return [d[m], i]
#            else:
#                d[n] = i

print(Solution().twoSum([2, 15, 11, 7], 9))
