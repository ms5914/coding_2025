class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.curr_index = 0
        # self.curr_left = self.encoding[self.curr_index] 

    def next(self, n: int) -> int:
        while self.curr_index<len(self.encoding)-1 and n > self.encoding[self.curr_index]:
            n-=self.encoding[self.curr_index]
            self.curr_index+=2
        
        if self.curr_index > len(self.encoding)-1:
            return -1
        self.encoding[self.curr_index]-=n
        return self.encoding[self.curr_index+1]
        


        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)