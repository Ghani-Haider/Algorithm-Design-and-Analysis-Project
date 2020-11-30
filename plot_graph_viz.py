import random
import graphviz

n = 1000
edges = []
nodes = []

file = open("test.txt", "w")
for i in range(n+1):
    nodes.append(i)
    edge_ = (random.randint(0,n-1), random.randint(0,n-1), random.randint(0,n))
    edges.append(edge_)
    file.write(str(edge_[0])+" "+str(edge_[1])+" "+str(edge_[2])+"\n")    
file.close()

# file = open("test.txt", "r")
# for line in file:
#     edge_ = line.strip().split()
#     edge_ = [int(i) for i in edge_]
#     # print((edge_[0],edge_[1],edge_[2]))
#     edges.append((edge_[0],edge_[1],edge_[2]))
# file.close()

## Prims ###
# G = []
# for i in range(n+1):
#     nodes.append(i)
# addNodes(G, nodes)
# addEdges(G, edges, False)
# time = prims(G)
# print("Prims in seconds = ",time)
# file_prims = open("prims.txt", "a")
# file_prims.write(str(n)+" "+str(time)+"\n")
# file_prims.close()

# ## Reverse ###
# g = Graph_R(n)
# for i in edges:
#     g.addEdge(i)
# r_time = g.reverseDeleteMST()
# print("Reverse-Del in seconds = ", r_time)
# file_Reverse = open("reverse.txt", "a")
# file_Reverse.write(str(n)+" "+str(r_time)+"\n")
# file_Reverse.close()

## Kruskal ###
# g = Graph_K(n)
# for i in edges:
#     g.addedge(i)

# k_time = g.kruskal_algo()
# print("Kruskal in seconds = ", k_time)
# file_kruskal = open("kruskal.txt", "a")
# file_kruskal.write(str(n)+" "+str(k_time)+"\n")
# file_kruskal.close()

def edge_print(edges):
    """Iterates over the edges in the graph.

    Args:
    - self: the instance to operate on.

    Returns:
    nothing.

    Yields:
    vertices in the graph.
    """
    for _edge in edges:
        yield ((str(_edge[0]), str(_edge[1])))

def visualize(edges, n) -> None:
    """Visualizes g.

    Args:
    - g: the graph/network to be visualized.

    Returns:
    Nothing.
    """
    e_lst = edges
    # Feel free to play around with the visualization.
    # Graphviz documentation: https://www.graphviz.org
    layout_engine = 'fdp' if n < 2000 else 'sfdp'
    # graph to be visualized
    vizgraph = graphviz.Graph(engine=layout_engine)
    _ = [vizgraph.node(str(v)) for v in range(n)]
    vizgraph.edges(edge_print(e_lst))
    vizgraph.render(view=True)


visualize(edges, n)

print("done")