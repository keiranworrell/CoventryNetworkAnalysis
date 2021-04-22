import networkx as nx
import matplotlib.pyplot as plt
import csv

# Change before use
deg_dist_path = "/Users/keiranworrell/Documents/Uni - 3rd Year/Dissertation/Data/degree_distribution.csv"
deg_weighted_dist_path = "/Users/keiranworrell/Documents/Uni - 3rd Year/Dissertation/Data/degree_distribution_weighted.csv"
cumulative_deg_dist_path = "/Users/keiranworrell/Documents/Uni - 3rd Year/Dissertation/Data/cumulative_degree_distribution.csv"


def get_degree_dist(G):
    weighted_degrees = {"degree": "frequency"}
    degrees = {"degree": "frequency"}
    for node in G.nodes():
        if G.degree(node) in degrees:
            degrees[G.degree(node)] = degrees[G.degree(node)] + 1
        else:
            degrees[G.degree(node)] = 1
    deg_weight = G.degree(weight="weight")
    for node in deg_weight:
        if node[1] in weighted_degrees:
            weighted_degrees[node[1]] = weighted_degrees[node[1]] + 1
        else:
            weighted_degrees[node[1]] = 1
    with open(deg_dist_path, "w") as f:
        w = csv.DictWriter(f, degrees.keys())
        w.writeheader()
        w.writerow(degrees)
    with open(deg_weighted_dist_path, "w") as f:
        w = csv.DictWriter(f, weighted_degrees.keys())
        w.writeheader()
        w.writerow(weighted_degrees)
    print("LOG: Degree distribution written to {}".format(deg_dist_path))
    print("LOG: Creating plot of degree distribution")
    plot_deg_dist(G)
    cumulative_deg_dist(degrees)


def plot_deg_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees, 150)
    plt.savefig("deg_dist.pdf")


def cumulative_deg_dist(degrees):
    new_degrees = {"degree": "frequency"}
    for key in degrees:
        if key != "degree":
            new_degrees[key] = degrees[key]
            for alt_key in degrees:
                if key != alt_key and alt_key != "degree":
                    if int(alt_key) < int(key):
                        new_degrees[key] = new_degrees[key] + degrees[alt_key]
    with open(cumulative_deg_dist_path, "w") as f:
        w = csv.DictWriter(f, new_degrees.keys())
        w.writeheader()
        w.writerow(new_degrees)