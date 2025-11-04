class RandomizedSet:

    def __init__(self):
        self.li = []
        self.hm = {}
        

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        self.li.append(val)
        self.hm[val] = len(self.li)-1
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.hm:
            return False
        ind = self.hm[val]
        last_val = self.li[len(self.li)-1]
        self.li[ind], self.li[len(self.li)-1] = self.li[len(self.li)-1], self.li[ind]
        self.hm[last_val] = ind
        self.li.pop()
        del self.hm[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.li)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()