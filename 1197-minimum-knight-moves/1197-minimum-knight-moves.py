class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(x,y):
            if x == 0 and y ==0:
                return 0
            elif x+y == 2: #(1,1),  (0,2), (2,0) 
                return 2
            else:
                return min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1)))+1
        return dfs(abs(x),abs(y))


        #Before explaining how we can apply the DFS algorithm to this problem, we should address the symmetry of the answers, which we haven't touched on so far.

# We claim that the target (x,y), its horizontally, vertically, and diagonally symmetric points (i.e. (x,−y),(−x,y),(−x,−y)) share the same answer as the target point.

# Due to the symmetry of the board (i.e. from -infinity to +infinity) and the symmetry of the allowed movements, we can rest assured that the above claim is correct, without rigid mathematical proof.

# Based on the above insight, we can focus on the first quadrant of the coordinate plane where both x and y are positive.
# Any target that is outside of the first quadrant, can be shifted to its symmetric point in the first quadrant by taking the absolute value of each coordinate, i.e. (∣x∣,∣y∣).