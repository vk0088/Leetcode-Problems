# Top down - Memoization
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        
        def dfs(dice, currSum):
            if dice == n:
                if currSum == target:
                    return 1 
                return 0
            
            if (dice, currSum) in memo:
                return memo[(dice, currSum)]
            
            ways = 0
            for i in range(1, k + 1):
                if currSum + i <= target:
                    ways += dfs(dice + 1, currSum + i)
                    ways %= (10**9 + 7)  
            
            memo[(dice, currSum)] = ways
            return ways
        
        return dfs(0, 0)

        