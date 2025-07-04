class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_count = {}
        for char in magazine:
            if char in magazine_count:
                magazine_count[char] += 1
            else:
                magazine_count[char] =1 for char in ransomNote:
            if char in magazine_count and magazine_count[char] > 0:
                magazine_count[char] -= 1
            else:
                return False
        
        return True