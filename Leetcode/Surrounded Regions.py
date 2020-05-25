class Solution:
    def solve(self, board: List[List[str]]) -> None:
        borderO = set()
        arr = []
        if(len(board) == 0):
            return
        for i in range(len(board[0])):
            if(board[0][i] == "O"):
                borderO.add((0, i))
                arr.append((0, i))
        for i in range(len(board[0])):
            if(board[len(board)-1][i] == "O"):
                borderO.add((len(board) - 1, i))
                arr.append((len(board) - 1, i))
        for j in range(len(board)):
            if(board[j][0] == "O"):
                borderO.add((j, 0))
                arr.append((j, 0))
        for j in range(len(board)):
            if(board[j][len(board[0])-1] == "O"):
                borderO.add((j, len(board[0])-1))
                arr.append((j, len(board[0]) - 1))
        ans = set()
        new = []
        while(True):
            if(len(arr) == 0):
                break
            for i in range(len(arr)):
                y = arr[i][0]
                x = arr[i][1]
                if((x + 1 < len(board[0])) and ((y, x+1) not in borderO) and (board[y][x+1] == "O")):
                    ans.add((y, x+1))
                    new.append((y, x+1))
                    borderO.add((y, x+1))
                if((x - 1 >= 0)and ((y, x-1) not in borderO) and (board[y][x-1] == "O")):
                    ans.add((y, x-1))
                    new.append((y, x-1))
                    borderO.add((y, x-1))
                if((y + 1 < len(board)) and ((y+1, x) not in borderO) and (board[y+1][x] == "O")):
                    ans.add((y+1, x))
                    new.append((y+1, x))
                    borderO.add((y+1, x))
                if((y - 1 >= 0)and ((y-1, x) not in borderO) and (board[y-1][x] == "O")):
                    ans.add((y-1, x))
                    new.append((y-1, x))
                    borderO.add((y-1, x))
            arr = new
            new = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == "O"):
                    if((i, j) not in borderO):
                        board[i][j] = "X"
        
                   
