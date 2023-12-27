class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        return self.nSum(nums, 3, 0, 0)  # Call the recursive function

    def nSum(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        length = len(nums)
        res = []

        if n < 2 or length < n:
            return res

        if n == 2:  # When the problem is reduced to two-sum
            l, r = start, length - 1
            while l < r:
                s = nums[l] + nums[r]
                left, right = nums[l], nums[r]
                if s < target:  # Move the left pointer
                    while l < r and nums[l] == left:
                        l += 1
                elif s > target:  # Move the right pointer
                    while l < r and nums[r] == right:
                        r -= 1
                else:  # Target combination found, de-duplicate and record
                    res.append([left, right])
                    while l < r and nums[l] == left:
                        l += 1
                    while l < r and nums[r] == right:
                        r -= 1
        else:  # When dealing with the sum of more numbers
            i = start
            while i < length:  # Iterate and de-duplicate
                sub = self.nSum(nums, n - 1, i + 1, target - nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
                while i < length - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
        return res