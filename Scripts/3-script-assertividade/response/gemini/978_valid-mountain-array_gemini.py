class Solution:
    def validMountainArray(self, A):
        n = len(A)
        if n < 3:
            return False
        i = 0
        while i + 1 < n and A[i] < A[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and A[i] > A[i + 1]:
            i += 1
        return i == n - 1