class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m = len(rooms)
        n = len(rooms[0])
        dq = deque()

        def should_visit(new_x, new_y):
            if new_x >= 0 and new_x < m and new_y>=0 and new_y<n and rooms[new_x][new_y] not in (-1, 0) and rooms[new_x][new_y] == 2147483647:
                return True
            return False


        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dq.append((i, j, 0))

        while dq:
            x, y, distance = dq.popleft()
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for i in range(len(dx)):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if should_visit(new_x, new_y):
                    print(new_x, new_y)
                    dq.append((new_x, new_y, distance+1))
                    rooms[new_x][new_y] = distance+1





        