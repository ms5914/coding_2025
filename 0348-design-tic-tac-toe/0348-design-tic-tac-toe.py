class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.left_diag = 0
        self.right_diag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        player = 1 if player == 1 else -1
        self.rows[row]+=player
        self.cols[col]+=player

        if row == col:
            self.left_diag+=player
        if row+col == self.n-1:
            self.right_diag+=player
        
        if player*self.n in (self.rows[row], self.cols[col], self.left_diag, self.right_diag):
            return 1 if player == 1 else 2
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)