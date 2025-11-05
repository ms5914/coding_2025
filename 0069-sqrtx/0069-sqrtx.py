class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1 or x == 2:
            return 1

        low = 2
        high = x // 2

        while low < high:
            mid = low + (high - low + 1) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid
            else:
                high = mid - 1
        return high
