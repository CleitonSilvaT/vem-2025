class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for p in 2, 3:
            while num % p == 0:
                num /= p