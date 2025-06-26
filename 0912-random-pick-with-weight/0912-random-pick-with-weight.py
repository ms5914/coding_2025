import random
from bisect import bisect_left

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        s = 0
        self.array = []
        for elem in w:
            s+=elem
            self.array.append(s)

    def pickIndex(self):
        """
        :rtype: int
        """
        return bisect.bisect_left(self.array, random.randint(1, self.array[-1]))



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()