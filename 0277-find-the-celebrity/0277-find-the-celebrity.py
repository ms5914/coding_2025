# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        potential_celebrity = 0
        
        for i in range(1, n):
            if knows(potential_celebrity, i):
                potential_celebrity = i
        
        for i in range(n):
            if i == potential_celebrity:
                continue
            if knows(potential_celebrity, i) or not knows(i, potential_celebrity):
                return -1
        return potential_celebrity
        