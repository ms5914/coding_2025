class DisjointSet:
    def __init__(self, m, n):
        self.parent = [i for i in range(m*n)]
        self.sizes = [1 for i in range(m*n)]
        
    
    def union(self, i, j):
        m, n = self.find_parent(i), self.find_parent(j)
        if m == n:
            return
        if self.sizes[m] < self.sizes[n]:
            self.parent[m] = n
            self.sizes[n]+=self.sizes[m]
        else:
            self.parent[n] = m
            self.sizes[m]+=self.sizes[n]
    
    def find_parent(self, i):
        print(i)
        if self.parent[i] != i:
            self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]




class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        matrix = [[0 for i in range(n)] for j in range(m)]
        dsu = DisjointSet(m, n)
        results = []
        num_islands = 0
        for i, j in positions:
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                dx = [0, 0, 1, -1]
                dy = [1, -1, 0, 0]
                different_islands = set()
                for k in range(len(dx)):
                    new_i = i+dx[k]
                    new_j = j+dy[k]

                    if new_i >=0 and new_i <m and new_j >=0 and new_j < n and matrix[new_i][new_j] == 1:
                        print(new_i, new_j)
                        different_islands.add(dsu.find_parent(new_i*n+new_j))
                        dsu.union(new_i*n + new_j, i*n+j)
                
                num_islands-=len(different_islands)
                num_islands+=1
            results.append(num_islands)
        return results
                    
                    

                    


        