class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1]*n      
        prev = [-1]*n  
        maxlen = 1      
        maxindex = 0    
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        prev[i] = j
            if dp[i] > maxlen:
                maxlen = dp[i]
                maxindex = i
        ans=[]
        while maxindex!=-1:
            ans.append(nums[maxindex])
            maxindex = prev[maxindex]
        return ans