class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child_i = 0
        cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i