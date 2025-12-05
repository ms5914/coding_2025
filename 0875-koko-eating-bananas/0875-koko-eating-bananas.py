class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat(speed):
            hours_needed = 0
            for pile in piles:
                hours_needed+=math.ceil(pile/speed)
            if hours_needed>h:
                return False
            return True
        
        low = 1
        high = max(piles)
        while low<high:
            mid = (low+high)//2
            if can_eat(mid):
                high = mid
            else:
                low = mid+1
        return low
    


        
        