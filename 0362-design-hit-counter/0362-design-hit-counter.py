class HitCounter:

    def __init__(self):
        self.dq = deque()
        self.result_sum = 0

    def hit(self, timestamp: int) -> None:
        if self.dq and self.dq[0][0] == timestamp:
            self.dq[0][1] +=1  
        else:
            self.dq.append([timestamp, 1])
        self.result_sum+=1
        
    def getHits(self, timestamp: int) -> int:
        
        while self.dq and self.dq[0][0] <= timestamp-300:
            _, count = self.dq.popleft()
            self.result_sum-=count
        
        print(self.dq, self.result_sum)
        return self.result_sum
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)