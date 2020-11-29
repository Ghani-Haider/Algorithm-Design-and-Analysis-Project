# Kruskal's algorithm in Python
import time

class Graph_K:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addedge(self, edge):
        self.graph.append(edge)

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        second_ini = time.time()
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1 and i < self.V:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        
        second_fin = time.time()
        return(second_fin-second_ini)
# # Driver Code 
# if __name__ == "__main__": 
  
#     # create the graph given in above fugure 
#     V = 5
#     g = Graph_K(V) 
  
#     # making above shown graph 
#     g.addedge((2, 0, 5)) 
#     g.addedge((0, 4, 1)) 
#     g.addedge((0, 1, 0)) 
#     g.addedge((4, 0, 3)) 
#     g.addedge((4, 0, 0)) 
#     g.addedge((4, 0, 0)) 
#     g.addedge((1, 1, 0)) 
#     g.addedge((1, 2, 1)) 
#     g.addedge((1, 4, 0)) 
#     g.addedge((2, 4, 2)) 
#     g.addedge((4, 2, 4)) 
#     g.addedge((0, 0, 2)) 
#     g.addedge((3, 1, 2)) 
#     g.addedge((1, 3, 3)) 
#     g.addedge((3, 1, 4)) 
#     print(g.kruskal_algo())