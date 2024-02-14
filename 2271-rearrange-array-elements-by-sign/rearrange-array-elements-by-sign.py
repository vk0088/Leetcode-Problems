class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        index_pos, index_neg = 0, 1

        for num in nums:
            if num > 0:
                ans[index_pos] = num
                index_pos += 2
            elif num < 0:
                ans[index_neg] = num
                index_neg += 2

        return ans