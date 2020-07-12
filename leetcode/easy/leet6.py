#https://leetcode.com/problems/jewels-and-stones/

#def numJewelsInStones(self, J, S):
#    return sum(map(J.count, S))
#def numJewelsInStones(self, J, S):
#    return sum(map(S.count, J))               # this one after seeing https://discuss.leetcode.com/post/244105
#def numJewelsInStones(self, J, S):
#    return sum(s in J for s in S)

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for x in J:
            for y in S:
                if x == y:
                    cnt += 1
        return cnt
    
print(Solution().numJewelsInStones("aA", "aAABBBB"))