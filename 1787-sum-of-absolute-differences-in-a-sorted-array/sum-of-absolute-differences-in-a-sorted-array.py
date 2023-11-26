class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tot, ans = 0, [sum(nums)] * n
        for i, val in enumerate(nums):
            ans[i] += tot - val * (n-i*2)
            tot -= 2*val
        return ans