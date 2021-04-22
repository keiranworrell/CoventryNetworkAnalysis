import networkx as nx
import matplotlib.pyplot as plt


def clustering(G):
    all_coefficients = [["degree", "clustering coefficients"]]
    all_edges = G.edges()
    for node in G:
        if G.degree(node) > 2:
            k = 0
            N = 0
            for nodei in G[node]:
                N += 1
                for edge in all_edges:
                    if edge[0] == nodei and edge[1] in G[node]:
                        k += 1
            c = (2 * k) / (N * (N - 1))

            placed = False
            for i in range(len(all_coefficients)):
                if all_coefficients[i][0] == G.degree(node):
                    all_coefficients[i][1].append(c)
                    placed = True
            if not placed:
                all_coefficients.append([G.degree(node), [c]])
    x = []
    y = []
    all_coefficients.pop(0)
    for i in range(len(all_coefficients)):
        x.append(all_coefficients[i][0])
        y.append(sum(all_coefficients[i][1]) / len(all_coefficients[i][1]))
    x_inv = []
    for val in x:
        x_inv.append(1 / val)
    plt.plot(x, y, "bx")
    x_inv = []
    x.sort()
    for val in x:
        x_inv.append(2.58 / val)
    plt.plot(x, x_inv, "r")
    plt.xlabel("Degree, k")
    plt.ylabel("Average clustering coefficient")
    plt.savefig("Plot_1.pdf")