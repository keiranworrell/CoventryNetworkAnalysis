import tkinter as tk
from tkinter import ttk
import csv


def unrecognisedCharacterPopUp(char):
    print("ERROR: Cannot record interaction for unrecognised character {}".format(char))
    win = tk.Toplevel()
    win.wm_title("Unrecognised Character: " + char)

    ttk.Label(win, text="The character {} was not recognised.".format(char)).grid(
        column=0, row=0, padx=10, pady=10
    )
    ttk.Label(
        win,
        text="Please record this character before including them in any interactions.",
    ).grid(column=0, row=1, padx=10, pady=10)

    ttk.Button(win, text="OK", command=win.destroy).grid(
        column=0, row=2, padx=20, pady=20
    )


def getCharacterID(char, nodes):
    for node in nodes:
        if char == node[1]:
            return node[0]
    return None


def createLink(c1, c2, type, pn, nodes, edges):
    char1 = c1.get()
    char2 = c2.get()
    page = pn.get()
    if char1 == char2:
        print("ERROR: Cannot record interaction between a character and themself.")
        return
    char1ID = getCharacterID(char1, nodes)
    char2ID = getCharacterID(char2, nodes)
    if char1ID == None:
        unrecognisedCharacterPopUp(char1)
    if char2ID == None:
        unrecognisedCharacterPopUp(char2)
    if char1ID == None or char2ID == None:
        return
    linkAlreadyExists = False
    for edge in edges:
        if (edge[0] == char1ID and edge[1] == char2ID and edge[4] == type) or (
            edge[1] == char1ID and edge[0] == char2ID and edge[4] == type
        ):
            if type == "hostile":
                edge[3] = int(edge[3]) + 1
            else:
                edge[3] = int(edge[3]) + 1
            linkAlreadyExists = True
            edge[5] = edge[5] + ", {}".format(page)
            break
    if not linkAlreadyExists:
        edges.append([char1ID, char2ID, "undirected", 1, type, str(page)])
    print(
        "LOG: Interaction between {} and {} logged on page {}".format(
            char1, char2, page
        )
    )


def newNode(char, pn, gen, nodes):
    character = char.get()
    if getCharacterID(character, nodes) == None:
        pageNum = pn.get()
        gender = gen.get()
        if len(nodes) == 1:
            id = 1
        else:
            id = int(nodes[-1][0]) + 1
        nodes.append([id, character, pageNum, gender])
        print("LOG: {} added to nodes.csv".format(character))
    else:
        print("ERROR: {} already present in nodes.csv".format(character))


def saveFile(nodes, edges, nodes_path, edges_path):
    nodes_path_save=nodes_path.strip('"')
    edges_path_save=edges_path.strip('"')
    with open(nodes_path_save, "a") as file:
        writer = csv.writer(file)
        writer.writerows(nodes)
    with open(edges_path_save, "a") as file:
        writer = csv.writer(file)
        writer.writerows(edges)
