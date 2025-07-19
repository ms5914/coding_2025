class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        q = deque()
        visited = set()
        
        q.append((0, 0, 1))
        visited.add((0, 0))

        while q:
            i, j, path = q.popleft()

            if i ==n-1 and j==n-1:
                return path

            delta = [(1, 1), (-1, -1), (0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1)]

            for direction in delta:
                new_i = i+direction[0]
                new_j = j+direction[1]
                if not (new_i, new_j) in visited  and new_i>=0 and new_i<=n-1 and new_j>=0 and new_j<=n-1 and grid[new_i][new_j] == 0:
                    q.append((new_i, new_j, path+1))
                    visited.add((new_i, new_j))
        return -1
            






        