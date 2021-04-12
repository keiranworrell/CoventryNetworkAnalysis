import networkx as nx
import csv

# Change before use
betweenness_path = (
    "/Users/keiranworrell/Documents/Uni - 3rd Year/Dissertation/Data/betweenness.csv"
)


def betweenness_centrality(G):
    betweenness = [["Character", "Betweenness Centrality"]]
    bc = nx.betweenness_centrality(G, normalized=True)
    names = nx.get_node_attributes(G, "name")
    for key in bc:
        betweenness.append([str(names[key]), str(bc[key])])
    with open(betweenness_path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(betweenness)
    print("LOG: Betweenness centrality written to: {}".format(betweenness_path))