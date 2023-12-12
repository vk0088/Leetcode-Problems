class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) -1
        current_max = global_max = -1
        while(j>i):
            current_max = (nums[i]-1) * (nums[j]-1)
            global_max = max(global_max,current_max)
            if nums[i] < nums[j]:
                i += 1
            elif nums[i] > nums[j]:
                j -= 1
            else:
                i += 1
                
            
            
        return global_max

        