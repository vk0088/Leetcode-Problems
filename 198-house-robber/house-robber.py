class Solution:
    def rob(self, nums: List[int]) -> int:
        chori1 = 0
        chori2 = 0
        if len(nums) == 0:
            return 0
        for num in nums:
            current = max(chori2 + num, chori1)
            chori2 = chori1
            chori1 = current
        return chori1