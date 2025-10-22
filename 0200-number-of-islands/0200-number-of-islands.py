class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            while q:
                (x, y) = q.popleft()
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1 ]
                
                for i in range(len(dx)):
                    
                    new_x = x+dx[i]
                    new_y = y+dy[i]
                    if new_x >= 0 and new_x < m and new_y<n and new_y>=0 and grid[new_x][new_y] == '1':
                        grid[new_x][new_y] = '0'
                        q.append((new_x, new_y))

        
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count+=1
                    bfs(i, j)
        
        return count
        