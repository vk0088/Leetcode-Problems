class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        def dfs(row_no,col_no):
            if row_no < 0 or row_no >= len(grid) or col_no < 0 or col_no >= len(grid[0]) or grid[row_no][col_no] == "0":
                return
            grid[row_no][col_no] = '0'
            dfs(row_no + 1, col_no)
            dfs(row_no - 1, col_no)
            dfs(row_no, col_no + 1)
            dfs(row_no, col_no -1)
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_island +=1
                    dfs(i,j)
        return num_island


        