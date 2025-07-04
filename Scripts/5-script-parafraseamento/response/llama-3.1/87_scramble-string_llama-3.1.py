class Solution:
    def isScramble(self, s1, s2):
        if len(s1)!= len(s2):
            return False
        if sorted(s1)!= sorted(s2):
            return False
        if len(s1) == 1:
            return True
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
               (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False