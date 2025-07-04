class Solution:
    def partitionLabels(self, S):
        result, last_seen, max_last_seen, count = [], {}, 0, 0
        for i, char in enumerate(S):
            last_seen[char] = i
        for i, char in enumerate(S):
            max_last_seen = max(max_last_seen, last_seen[char])
            count += 1
            if i == max_last_seen:
                result.append(count)
                count = 0
        return result