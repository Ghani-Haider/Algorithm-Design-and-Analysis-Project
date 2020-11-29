import matplotlib.pyplot as plt

def fileRead(filename):
    f = open(filename,"r")
    file = f.readlines()
    values = [val.split() for val in file]
    x = [int(val[0]) for val in values]
    y = [round(float(val[1]),2) for val in values]
    return [x,y]
    

def plot():
    prims = fileRead("prims.txt")
    kruskal = fileRead("kruskal.txt")
    reverse = fileRead("reverse.txt")
    plt.plot(prims[0], prims[1], label="Prims")
    plt.plot(kruskal[0], kruskal[1], label="Kruskal")
    plt.plot(reverse[0], reverse[1],label="Reverse Delete")
    plt.legend()
    plt.xlabel("Number of Vertices")
    plt.ylabel("Run time / s")
    plt.show()



        
plot()