class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.curr_i = 0
        self.curr_j = 0
    
    def next(self) -> int:
        while self.curr_i < len(self.vec) and self.curr_j > len(self.vec[self.curr_i])-1:
            if self.curr_j > len(self.vec[self.curr_i])-1:
                self.curr_i = self.curr_i+1
                self.curr_j = 0
                
        val = self.vec[self.curr_i][self.curr_j]
        self.curr_j = self.curr_j+1 
        return val
    
    def hasNext(self) -> bool:
        while self.curr_i < len(self.vec) and self.curr_j > len(self.vec[self.curr_i])-1:
            if self.curr_j > len(self.vec[self.curr_i])-1:
                self.curr_i = self.curr_i+1
                self.curr_j = 0
                
        return self.curr_i <= len(self.vec)-1 and self.curr_j <= len(self.vec[self.curr_i])-1