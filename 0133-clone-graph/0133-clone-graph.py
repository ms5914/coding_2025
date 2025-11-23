"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def clone(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            new_node = Node(node.val)
            visited[node] = new_node
            new_neighbors = []
            for i in range(len(node.neighbors)):
                nei = clone(node.neighbors[i])
                new_neighbors.append(nei)
            new_node.neighbors = new_neighbors
            return new_node
        
        return clone(node)
            
            


        
        