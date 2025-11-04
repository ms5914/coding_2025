class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diagonal = 0
        self.antidiagonal = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        
        to_add = 1 if player == 1 else -1
        
        self.rows[row]+=to_add
        self.cols[col]+=to_add
        
        if row == col:
            self.diagonal+=to_add
        if row+col == self.n-1:
            self.antidiagonal+=to_add
        
        if self.rows[row] == to_add*self.n or self.cols[col] == to_add*(self.n) or self.diagonal == to_add*self.n or self.antidiagonal == to_add*self.n:
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
