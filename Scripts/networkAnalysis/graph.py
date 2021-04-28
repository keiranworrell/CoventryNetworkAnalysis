import networkx as nx
import matplotlib.pyplot as plt
import csv
from networkAnalysis.clusteringCoeff import clustering
from networkAnalysis.degree_distribution import get_degree_dist
from networkAnalysis.betweenness_centrality import betweenness_centrality
from networkAnalysis.remove_character import remove_character
from networkAnalysis.giant_stability import test_giant_stability,get_giant_component
from networkAnalysis.assortativity import get_assortativity
from networkAnalysis.friendly_hostile_network import create_friendly_hostile_graph

def Analysis(nodes, edges, nodes_path, edges_path):
    # Generate the network from nodes and edges lists
    print("LOG: Generating network")
    G = nx.Graph()
    for node in nodes[1:]:
        G.add_node(node[0], name=str(node[1]), gender=str(node[3]))
    for edge in edges[1:]:
        G.add_edge(edge[0], edge[1], weight=int(edge[3]), friendly_hostile=str(edge[4]))
    r, r_friendly = get_assortativity(G)
    m, f, unknown = count_genders(G)
    giant = get_giant_component(G)
    print("With Shaka:")
    print(
        "Number of nodes = {}\nNumber of edges = {}\nDegree assortativity = {}\nDegree assortativity for friendly network = {}\nMale characters = {}\nFemale characters = {}\nCharacter with unknown gender = {}\nGiant component = {}\n".format(
            G.number_of_nodes(),
            G.number_of_edges(),
            r,
            r_friendly,
            m,
            f,
            unknown,
            giant,
        )
    )

    G_noShaka = remove_character(G, "Shaka", nodes_path, edges_path)
    r_noShaka, r_friendly_noShaka = get_assortativity(G_noShaka)
    m_noShaka, f_noShaka, unknown_noShaka = count_genders(G_noShaka)
    giant_noShaka = get_giant_component(G_noShaka)
    print("Without Shaka:")
    print(
        "Number of nodes = {}\nNumber of edges = {}\nDegree assortativity = {}\nDegree assortativity for friendly network = {}\nMale characters = {}\nFemale characters = {}\nCharacter with unknown gender = {}\nGiant component = {}\n".format(
            G_noShaka.number_of_nodes(),
            G_noShaka.number_of_edges(),
            r_noShaka,
            r_friendly_noShaka,
            m_noShaka,
            f_noShaka,
            unknown_noShaka,
            giant_noShaka,
        )
    )
    betweenness_centrality(G)
    get_degree_dist(G)
    clustering(G)
    test_giant_stability(G)

    hostileG = create_friendly_hostile_graph(G, "Hostile")
    m_hostile, f_hostile, unknown_hostile = count_genders(hostileG)
    print("\nHostile Network:")
    print(
        "Number of nodes = {}\nNumber of edges = {}\nMale characters = {}\nFemale characters = {}\nCharacter with unknown gender = {}\n".format(
            hostileG.number_of_nodes(),
            hostileG.number_of_edges(),
            m_hostile,
            f_hostile,
            unknown_hostile
        )
    )

def plotGraph(G):
    d = dict(G.degree)
    labels = nx.get_node_attributes(G, "name")
    nx.draw(
        G, nodelist=d.keys(), node_size=[v * 100 for v in d.values()], labels=labels
    )
    plt.show()


def count_genders(G):
    male = 0
    female = 0
    unknown = 0
    for node in G.nodes.data("gender"):
        if node[1] == "M":
            male += 1
        elif node[1] == "F":
            female += 1
        else:
            unknown += 1
    return (male, female, unknown)
