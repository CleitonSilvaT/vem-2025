class Solution:
    def numJewelsInStones(self, J, S):
        return sum(S.count(j) for j in J)