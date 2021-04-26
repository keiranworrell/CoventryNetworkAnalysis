import networkx as nx


def create_friendly_hostile_graph(G, type):
    tempG = nx.create_empty_copy(G)
    for edge in G.edges.data("friendly_hostile"):
        if edge[2] == type:
            tempG.add_edge(edge[0], edge[1])
    toRemove = []
    for node in tempG.nodes():
        if tempG.degree(node) == 0:
            toRemove.append(node)
    for node in toRemove:
        tempG.remove_node(node)
    return tempG