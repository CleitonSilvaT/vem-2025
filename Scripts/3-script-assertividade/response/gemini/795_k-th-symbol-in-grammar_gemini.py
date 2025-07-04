class Solution:
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        if k <= (2**(n - 2)):
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - (2**(n - 2)))