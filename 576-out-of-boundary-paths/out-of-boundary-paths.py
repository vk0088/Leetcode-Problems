from functools import lru_cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        mod = 1000000007
        @cache
        def dfs(i,j,count):
            
            # print("position", i,j,count)
            if i < 0 or i == m or j < 0 or j == n:
                # print("out of boundary",i,j)
                return 1
            if count == maxMove:
                return 0
            
            return (dfs(i-1,j,count+1) + dfs(i+1,j,count+1)
                + dfs(i,j-1,count+1) + dfs(i,j+1,count+1)) % mod
        
        # dp = [[0]*m for _ in range(n)]
        return dfs(startRow,startColumn,0)
        