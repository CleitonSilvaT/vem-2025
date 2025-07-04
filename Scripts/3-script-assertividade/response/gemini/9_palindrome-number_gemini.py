class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_x = 0
        original_x = x
        
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        
        return reversed_x == original_x