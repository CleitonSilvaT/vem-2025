class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n  
        while left < right:
            mid = left + (right - left) // 2  
            if isBadVersion(mid):
                right = mid  
            else:
                left = mid + 1  
        return left  