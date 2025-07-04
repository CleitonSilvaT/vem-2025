class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        return reversed_x