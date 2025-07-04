class Solution:
    def integerBreak(self, n):
        dp = [None, 1]
        for i in range(2, n + 1):
            dp.append(0)
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]