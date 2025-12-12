class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # timestamps = [t for t, v in self.hm[key]]
        index = bisect.bisect_right(self.hm[key], timestamp, key=lambda x: x[0])
        if index == 0:
            return ""
        else:
            return self.hm[key][index-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)