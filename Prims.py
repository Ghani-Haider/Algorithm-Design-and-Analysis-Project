def addNodes(G,nodes):
    for _ in range(len(nodes)):
        row=[]
        for _ in range(len(nodes)):
            row.append(0)
        G.append(row)
    return G


def addEdges(G,edges,directed):
    for i in edges:
        if directed:      
            G[i[0]][i[1]]=i[2]        
        else:
            G[i[0]][i[1]]=i[2]
            G[i[1]][i[0]]=i[2]
    return G


def prims(G):
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
                minimum_index = v
        # Update weight of minimum node
        MSTset[minimum_index] = True
        # Update neighbours of picked node with shortest distance
        for v in range(nodes):
            if G[minimum_index][v] > 0 and MSTset[v] == False and weights[v] > G[minimum_index][v]:
                weights[v] = G[minimum_index][v]
                MST[v] = minimum_index
    # Display MST
    for i in range(1, nodes):
        print(MST[i], "-",i,"\t",G[i][MST[i]])


# nodes=[0,1,2,3,4,5]
# edges=[(0,1,4),(0,2,2),(1,2,4),(2,3,3), (2,4,2), (2,5,4), (3,5,3), (4,5,3)]
nodes = [0,1,2,3]
edges = [(0,1,3), (0,3,5), (1,2,1), (2,3,2)]
G=[]
addNodes(G,nodes)
addEdges(G,edges,False)
# print(G)
prims(G)