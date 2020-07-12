#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for x in range(len(nums)):
            cnt = 0
            for y in nums:
                if nums[x] > y:
                    cnt += 1
            res.append(cnt)
        return res

print(Solution().smallerNumbersThanCurrent([6,5,4,8]))