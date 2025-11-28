class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:



        m = len(grid)
        n = len(grid[0])
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1
        visited = set()

        def isvisitable(new_x, new_y):
            return new_x>=0 and new_x<m and new_y>=0 and new_y<n and grid[new_x][new_y] == 0 and not (new_x, new_y) in visited

        
        q = deque()
        q.append(((0, 0), 1))
        visited.add((0,0))

        while q:
            points, distance = q.popleft()
            x, y = points[0], points[1]
            if x == m-1 and y == n-1:
                return distance
            dx = [0, 0, 1, -1, 1, 1, -1, -1]
            dy = [1, -1, 0, 0, -1, 1, 1, -1]

            for i in range(len(dx)):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if isvisitable(new_x, new_y):
                    q.append(((new_x, new_y), distance+1))
                    visited.add((new_x, new_y))
        
        return -1


            

