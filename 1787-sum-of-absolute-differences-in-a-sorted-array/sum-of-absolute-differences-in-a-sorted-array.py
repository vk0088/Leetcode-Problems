class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        result = []

        for index, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            left_sum += num

            sum_left_side = num * index - left_sum + num
            sum_right_side = right_sum - num * (len(nums) - index - 1)

            result.append(sum_left_side + sum_right_side)

        return result