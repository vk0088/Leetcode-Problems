import operator
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        s = 0
        for i in nums:
            d[i] = 0
        for j in nums:
            d[j] = d[j] + 1
        m = max(d.values())
        for i in d:
            if d[i] == m:
                s = s+d[i]
        return s
        