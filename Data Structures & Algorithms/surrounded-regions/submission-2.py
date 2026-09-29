class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 

            if board[r][c] !="O":
                return 

            board[r][c]="S"

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        # find all O's connected to the boundary
        for r in range(rows):
            dfs(r, 0)       #left
            dfs(r, cols-1)  #right

        for c in range(cols):
            dfs(0, c)       #top
            dfs(rows-1, c)  #bottom

        #convert surrounded O's to X
        #convert safe S's back to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
