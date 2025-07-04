class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = 0
        result = ''
        for i in range(max_len - 1, -1, -1):
            digit_sum = int(a[i]) + int(b[i]) + carry
            result = str(digit_sum % 2) + result
            carry = digit_sum // 2
        if carry:
            result = '1' + result
        return result