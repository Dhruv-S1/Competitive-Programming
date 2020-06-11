class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(key):
            temp = [key]
            new = []
            visited.add(key)
            rowLen = len(grid)
            colLen = len(grid[0])
            while(True):
                if(temp == []):
                    break
                for i in range(len(temp)):
                    row = temp[i][0]
                    col = temp[i][1]
                    if(row + 1 < rowLen and (row+1, col) not in visited):
                        if(grid[row+1][col] == '1'):
                            visited.add((row+1, col))
                            new.append((row+1, col))
                    if(row - 1 >= 0 and (row-1, col) not in visited):
                        if(grid[row-1][col] == '1'):
                            visited.add((row-1, col))
                            new.append((row-1, col))
                    if(col + 1 < colLen and (row, col+1) not in visited):
                        if(grid[row][col+1] == '1'):
                            visited.add((row, col+1))
                            new.append((row, col+1))
                    if(col - 1 >= 0 and (row, col-1) not in visited):
                        if(grid[row][col-1] == '1'):
                            visited.add((row, col-1))
                            new.append((row, col-1))
                temp = []
                temp = new
                new = []
                    
                
        
        
        ones = set()
        visited = set()
        for i in range(len(grid)):    # O(n*m)
            for j in range(len(grid[i])):
                if(grid[i][j] == '1'):
                    ones.add((i, j))
        islands = 0
        for key in ones:    # O(nm)
            if(key not in visited):
                bfs(key)   # O(mn)
                islands += 1
        return islands
        
