class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        count=0
        m=len(grid)
        n=len(grid[0])
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 1:
                return
            grid[i][j]=1
            dfs(i+1, j) 
            dfs(i-1, j)
            dfs(i, j+1) 
            dfs(i, j-1) 
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and grid[i][j]==0:
                    dfs(i,j)

        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j]==0:
                    count+=1
                    dfs(i,j)
                        
        return count