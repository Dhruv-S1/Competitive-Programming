class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        longest = 0
        row = len(grid)
        col = len(grid[0])
        def dfs(node):
            i = node[0]
            j = node[1]
            ans = 0
            if(i+1<row and grid[i+1][j] and ((i+1, j) not in visited)):
                visited.add((i+1, j))
                ans+= dfs((i+1, j))
            if(i-1>=0 and grid[i-1][j] and ((i-1, j) not in visited)):
                visited.add((i-1, j))
                ans+= dfs((i-1, j))
            if(j+1<col and grid[i][j+1] and ((i, j+1) not in visited)):
                visited.add((i, j+1))
                ans+= dfs((i, j+1))
            if(j-1>=0 and grid[i][j-1] and ((i, j-1) not in visited)):
                visited.add((i, j-1))
                ans+= dfs((i, j-1))
            return ans+1
                
                
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 1):
                    if((i, j) not in visited):
                        visited.add((i, j))
                        temp = dfs((i, j))
                        if(temp > longest):
                            longest = temp

        return longest
                    
