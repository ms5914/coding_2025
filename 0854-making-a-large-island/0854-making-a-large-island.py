class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.island_sizes = [1 for _ in range(n)]
    
    def find_parent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
            
    
    def union(self, node1, node2):
        parent1 = self.find_parent(node1)
        parent2 = self.find_parent(node2)
        if parent1 == parent2:
            return
        else:
            if self.island_sizes[parent1] <= self.island_sizes[parent2]:
                self.parent[parent1] = parent2
                self.island_sizes[parent2] += self.island_sizes[parent1]
            else:
                self.parent[parent2] = parent1
                self.island_sizes[parent1] += self.island_sizes[parent2]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        num_nodes = m*n
        dsu = DSU(num_nodes)
        max_island_size = 0

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr_coord = n*i+j
                    for k in range(len(dx)):
                        new_i = i + dx[k]
                        new_j = j + dy[k]
                        if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] == 1:
                            new_coord = new_i * n + new_j
                            dsu.union(new_coord, curr_coord)

        max_size = max(dsu.island_sizes)
        for i in range(m):
            for j in range(n):
                roots = set()
                if grid[i][j] == 0:
                    curr_coord = n*i+j
                    for k in range(len(dx)):
                        new_i = i + dx[k]
                        new_j = j + dy[k]
                        if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] == 1:
                            roots.add(dsu.find_parent(n*new_i+new_j))
                
                curr_size = 1
                for root in roots:
                    curr_size+=dsu.island_sizes[root]
                
                max_size = max(max_size, curr_size)
        return max_size

                
                            


        
        


            

                            

                            



                    




        