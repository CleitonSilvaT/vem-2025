class Solution:
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True  
        if sorted(s1) != sorted(s2):
            return False  
        n = len(s1)
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
               (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True  
        return False  