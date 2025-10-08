class Solution:
    def reverseBits(self, n: int) -> int:
        number = 0
        k = 31
        while n:
            number += (n&1)<<k
            k-=1
            n = n>>1
        return number
            