import networkx as nx
from random import choice


def test_giant_stability(G):
    important_chars = [
        "Shaka",
        "Mdlaka",
        "Dingiswayo",
        "Zwide",
        "Mgobozi",
        "Nandi",
        "Senzangakona",
    ]
    for char in important_chars:
        g = test_stability_without(G, char)
        print(
            "Without {}, G has giant component with size {} ({} %)".format(
                char, g, g * 100 / (G.number_of_nodes() - 1)
            )
        )

    print("LOG: Checking giant component size when random nodes are removed.")
    average_gc_size = 0
    i=0
    while i < 50:
        nodes = list(G.nodes(data="name"))
        random_node = choice(nodes)
        average_gc_size += test_stability_without(G, random_node[1])
        i += 1

    average_gc_size = average_gc_size / 50
    print(
        "Average giant component size when random nodes removed = {}".format(
            average_gc_size
        )
    )


def test_stability_without(G, char):
    G_temp = G.copy()
    for node in G.nodes(data="name"):
        if str(node[1]) == str(char):
            G_temp.remove_node(node[0])
            break
    giant = get_giant_component(G_temp)
    return giant


def get_giant_component(G):
    giant = max(nx.connected_components(G), key=len)
    return len(giant)