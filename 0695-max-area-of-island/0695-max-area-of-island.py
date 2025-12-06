class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def find_area(i, j):
            grid[i][j] = 0
            q = deque()
            q.append([i, j])
            count = 1
            while q:
                x, y = q.popleft()
                
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]

                for ind in range(len(dx)):
                    new_x = x + dx[ind]
                    new_y = y + dy[ind]

                    if new_x>=0 and new_x<m and new_y>=0 and new_y<n and grid[new_x][new_y] == 1:
                        count+=1
                        grid[new_x][new_y] = 0
                        q.append([new_x, new_y])
            return count

        max_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_count = max(max_count, find_area(i, j))
        return max_count
                    
    




        
        
        