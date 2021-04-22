import networkx as nx
import csv


def remove_character(G, toRemove, nodes_path, edges_path):
    print("LOG: Removing {} from graph".format(toRemove))
    temp_nodes = []
    temp_edges = []

    tempG = G.copy()
    for node in G.nodes(data="name"):
        if str(node[1]) == str(toRemove):
            tempG.remove_node(node[0])
            break

    temp_nodes.insert(0, ["ID", "Name", "Page introduced", "Gender"])
    temp_edges.insert(
        0, ["Source", "Target", "Type", "Weight", "Friendly/Hostile", "Pages"]
    )
    for node in tempG.nodes(data=True):
        temp_nodes.append([node[0], node[1]["name"], "NA", node[1]["gender"]])
    for edge in tempG.edges(data=True):
        temp_edges.append(
            [
                edge[0],
                edge[1],
                "undirected",
                edge[2]["weight"],
                edge[2]["friendly_hostile"],
                "NA",
            ]
        )

    new_node_path = ("/".join(nodes_path.split("/")[:-1])) + "/nodes_no{}.csv".format(
        toRemove
    )
    new_edge_path = ("/".join(edges_path.split("/")[:-1])) + "/edges_no{}.csv".format(
        toRemove
    )

    with open(new_node_path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(temp_nodes)
    with open(new_edge_path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(temp_edges)
    return tempG