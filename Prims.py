import time

def addNodes(G,nodes):
    for i in nodes:
        if i not in G.keys():
            G[i]=[]
    return G

def addEdges(G,edges,directed):
    for i in edges:
        if directed:
            G[i[0]].append((i[1],i[2]))
        else:
            G[i[0]].append((i[1],i[2]))
            G[i[1]].append((i[0],i[2]))
    return G

def prims(G):
    second_ini = time.time()
    nodes = len(G)
    # picks minimum weighted edge from this
    weights = [float('inf')]* nodes
    # Array to store constructed MST
    MST = [None] * nodes
    # First node = root node
    MST[0] = -1
    # Starting vertex initialised to 0 so MST starts from first node
    weights[0] = 0
    # All non visited nodes initialised to False
    MSTset = [False] * nodes
    for _ in range(nodes):
        Min = float('inf')
        # Finds minimum weighted vertex which is not yet visited
        for v in range(nodes):
            if weights[v] < Min and MSTset[v] == False:
                Min = weights[v]
                minimum_value = v
        # Update weight of minimum node
        MSTset[minimum_value] = True
        # Update neighbours of picked node with shortest distance
        for v in G[minimum_value]:
            if v[1] > 0 and MSTset[v[0]] == False and weights[v[0]] > v[1]:
                weights[v[0]] = v[1]
                MST[v[0]] = minimum_value
    second_fin = time.time()
    return(second_fin-second_ini)

# nodes=[0,1,2,3,4,5]
# edges=[(0,1,4),(0,2,2),(1,2,4),(2,3,3), (2,4,2), (2,5,4), (3,5,3), (4,5,3)]
# nodes = [0,1,2,3,4,5,6,7,8]
# edges = [(7,8,7), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (0, 1, 4)]
# G={}
# addNodes(G,nodes)
# addEdges(G,edges,False)

# print(G)
# prims(G)