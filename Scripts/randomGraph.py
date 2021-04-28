import networkx as nx

n = 176
mean_degree = 5.011
# Number of edges
m = (n * mean_degree) / 2


def random_graph(n, m):
    G = nx.gnm_random_graph(n, m)
    if nx.is_connected(G):
        sum_of_degrees = 0
        average_path_length = nx.average_shortest_path_length(G)

        clustering_coefficient = nx.average_clustering(G)
        return (average_path_length, clustering_coefficient)
    else:
        # Recursively generate new graph if not connected
        return random_graph(n, m)


total_path_length = 0
total_clustering = 0
for i in range(100):
    path_length, clustering = random_graph(n, m)
    total_path_length += path_length
    total_clustering += clustering

print(
    "Average path length = {}\n Average clustering coefficient = {}".format(
        total_path_length / 100, total_clustering / 100
    )
)
