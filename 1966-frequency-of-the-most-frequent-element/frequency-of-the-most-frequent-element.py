class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left ,right = 0, 0
        totalSum = 0
        maxLength = 0
        while right < len(nums):
            rv = nums[right]
            totalSum += rv
            while (right - left + 1) * nums[right] - totalSum > k:
                rl = nums[left]
                totalSum -= nums[left]
                left += 1
            maxLength = max(maxLength, right - left + 1)
            right += 1
        return maxLength