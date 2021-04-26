import networkx as nx
import csv
import matplotlib.pyplot as plt
import numpy as np

# Change before use
clustering_path = (
    "/Users/keiranworrell/Documents/Uni - 3rd Year/Dissertation/Data/clustering_dist.csv"
)

def bestfit(x):
    y=0.2743+(2.58/x)
    return y

def clustering(G):
    clusteringCoeffs = [["Degree", "Number of Nodes", "Total Clustering Coefficient"]]
    c = nx.clustering(G)
    for key in c:
        degree = G.degree(key)
        degree_not_present = True
        for i in range(len(clusteringCoeffs)):
            if clusteringCoeffs[i][0] == str(degree):
                clusteringCoeffs[i][1] = str(int(clusteringCoeffs[i][1])+1)
                clusteringCoeffs[i][2] = str(float(clusteringCoeffs[i][2])+c[key])
                degree_not_present = False
        if degree_not_present:
            clusteringCoeffs.append([str(degree), "1", str(c[key])])

    with open(clustering_path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(clusteringCoeffs)
    print("LOG: Clustering coefficient distribution written to: {}".format(clustering_path))
    x = []
    y = []
    for deg in clusteringCoeffs[1:]:
        if (deg[0] != 1):
            x.append(float(deg[0]))
            y.append(float(deg[2])/float(deg[1]))
    plt.clf()
    plt.plot(x, y, 'ro')
    plt.grid()
    plt.xlabel("Degree, $k$")
    plt.ylabel("Mean clustering coefficient, $C(k)$")
    plt.title("A plot of degree $k$ against the mean clustering coefficient for that\ndegree, $C(k)$, with fitted curve $C(k)=0.2743+2.58k^{-1}$")
    x = np.linspace(1, 110, 1000)
    y = bestfit(x)
    plt.plot(x,y,'b')
    plt.savefig("clusterCoeff.pdf")
