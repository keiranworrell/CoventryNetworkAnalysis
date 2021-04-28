import csv
import tkinter as tk
from tkinter import ttk
from functools import partial
from os import path
from networkAnalysis.graph import Analysis
from uiBuilder.startUI import startUI

function = int(input("Data Collection (1) or Network Analysis (2)?\n"))

# Populate before use
nodes_path = ""
edges_path = ""

# If csv files exist, read data. Else, set edges and nodes
if path.exists(nodes_path):
    print("LOG: Nodes path exists, extracting data")
    with open(nodes_path, "r") as f:
        reader = csv.reader(f)
        nodes = list(reader)
else:
    nodes = [["ID", "Name", "Page introduced", "Gender"]]

if path.exists(edges_path):
    print("LOG: Edges path exists, extracting data")
    with open(edges_path, "r") as f:
        reader = csv.reader(f)
        edges = list(reader)
else:
    edges = [["Source", "Target", "Type", "Weight", "Friendly/Hostile", "Pages"]]

# If csv files exist but are empty, populate with headings
if len(nodes) < 1:
    nodes = [["ID", "Name", "Page introduced", "Gender"]]
if len(edges) < 1:
    edges = [["Source", "Target", "Type", "Weight", "Friendly/Hostile", "Pages"]]


if function == 1:
    # Start GUI to collect data and add nodes/edges to lists
    startUI(nodes, edges, nodes_path, edges_path)
elif function == 2:
    # Run function in graph.py
    Analysis(nodes, edges, nodes_path, edges_path)
