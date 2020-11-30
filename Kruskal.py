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
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        for each_edge in self.graph:
            u, v, w = each_edge
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        
        second_fin = time.time()
        return(second_fin-second_ini)

# # Driver Code 
# if __name__ == "__main__": 
  
#     # create the graph given in above fugure 
#     V = 9
#     g = Graph_K(V) 
  
#     # making above shown graph 
#     g.addedge((0, 1, 4)) 
#     g.addedge((0, 7, 8)) 
#     g.addedge((1, 2, 8)) 
#     g.addedge((1, 7, 11)) 
#     g.addedge((2, 3, 7)) 
#     g.addedge((2, 8, 2)) 
#     g.addedge((2, 5, 4)) 
#     g.addedge((3, 4, 9)) 
#     g.addedge((3, 5, 14)) 
#     g.addedge((4, 5, 10)) 
#     g.addedge((5, 6, 2)) 
#     g.addedge((6, 7, 1)) 
#     g.addedge((6, 8, 6)) 
#     g.addedge((7, 8, 7))
#     g.kruskal_algo()