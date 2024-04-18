class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
                
        grid_pad = [[0]*(m+2)]
        for i, row in enumerate(grid):
            row.insert(0, 0)
            row.extend([0])
            grid_pad.append(row)
        grid_pad.append([0]*(m+2))

        # perimenter = 0
        # # Apply convolutional filter that count the transitions
        # # first by row, then by columns
        transitions = 0
        for i, row in enumerate(grid_pad):
            print(transitions)
            if i == n + 1:
                break
            for j, ele in enumerate(row): 
                if j == m + 1:
                    break
                if ele: # element at position i,j is 1
                    # transition down
                    if grid_pad[i][j+1] == 0: 
                        transitions+=1
                    if grid_pad[i+1][j] == 0: 
                        transitions+=1

                else:
                    # transition up
                    if grid_pad[i][j+1] == 1:
                        transitions+=1
                    if grid_pad[i+1][j] == 1:
                        transitions+=1
                    
        return transitions

    def islandPerimeter_broken(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
                
        # grid_pad = [[0]*(m+2)]
        # for i, row in enumerate(grid):
        #     row.insert(0, 0)
        #     row.extend([0])
        #     grid_pad.append(row)
        # grid_pad.append([0]*(m+2))

        # perimenter = 0
        # # Apply convolutional filter that count the transitions
        # # first by row, then by columns
        transitions = 0

        def onTheBorder(i,j,n,m):
            return i==0 or j==0 or i==n-1 or j==m-1 


        for i, row in enumerate(grid):
            for j, ele in enumerate(row): 
                if ele and onTheBorder(i,j,n,m):
                    transitions+=1
                if j == m-1 or i == n-1:
                    break

                if ele: # current element at i, j is 1
                    # transition down
                    if grid[i][j+1] == 0: 
                        transitions+=1
                    if grid[i+1][j] == 0: 
                        transitions+=1

                else: # current element is 0 

                    # transition up
                    if grid[i][j+1] == 1:
                        transitions+=1
                    if grid[i+1][j] == 1:
                        transitions+=1

        return transitions


    
        