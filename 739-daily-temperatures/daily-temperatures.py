class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = []
        ans = [0]*n
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:
                ans[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return ans
                
            

        