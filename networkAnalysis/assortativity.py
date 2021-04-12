import networkx as nx


def get_assortativity(G):
    # Set assortativity of complete graph
    r = nx.degree_assortativity_coefficient(G)

    # Remove hostile links from network
    tempG = nx.create_empty_copy(G)
    for edge in G.edges.data("friendly_hostile"):
        if edge[2] == "Friendly":
            tempG.add_edge(edge[0], edge[1])
    r_friendly = nx.degree_assortativity_coefficient(tempG)
    return (r, r_friendly)
