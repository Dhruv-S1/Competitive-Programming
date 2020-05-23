class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        totalOranges = 0
        rotten = []
        visited = set()
        length = len(grid)
        width = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 1):
                    totalOranges += 1
                if(grid[i][j] == 2):
                    totalOranges += 1
                    rotten.append((i, j))
                    visited.add((i, j))
        time = 0
        new = []
        while(True):
            if(totalOranges == len(visited)):
                return time
            if(len(rotten) == 0):
                return -1
            for i in range(len(rotten)):
                x = rotten[i][1]
                y = rotten[i][0]
                if(x + 1 < width and (y, x+1) not in visited):
                    if(grid[y][x+1] == 1):
                        new.append((y, x+1))
                        visited.add((y, x+1))
                if(x - 1 >= 0 and (y, x-1) not in visited):
                    if(grid[y][x-1] == 1):
                        new.append((y, x-1))
                        visited.add((y, x-1))
                if(y + 1 < length and (y+1, x) not in visited):
                    if(grid[y+1][x] == 1):
                        new.append((y+1, x))
                        visited.add((y+1, x))
                if(y - 1 >= 0 and (y-1, x) not in visited):
                    if(grid[y-1][x] == 1):
                        new.append((y-1, x))
                        visited.add((y-1, x))
            time += 1
            rotten = new
            new = []
                
                         
                    
                

            
        
        
