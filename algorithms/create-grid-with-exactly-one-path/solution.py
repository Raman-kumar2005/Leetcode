class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        def dfs(i,j):
            
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0
            sum_=grid[i][j]
            grid[i][j]=0
            sum_+=dfs(i+1,j)
            sum_+=dfs(i-1,j)
            sum_+=dfs(i,j+1)
            sum_+=dfs(i,j-1)
            return sum_
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    if dfs(i,j)%k==0:
                        count+=1
        return count
