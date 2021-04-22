import tkinter as tk
from tkinter import ttk
from functools import partial
from uiBuilder.UI_actions import createLink,newNode,saveFile


def startUI(nodes, edges, nodes_path, edges_path):
    print("Starting data collection UI")
    # Create window with tabs
    root = tk.Tk()
    root.title("Data Collection")
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text="Record character")
    tabControl.add(tab2, text="Record interaction")

    # Populate interaction tab
    char1 = tk.StringVar()
    char2 = tk.StringVar()
    pageNum = tk.StringVar()

    ttk.Label(tab2, text="Character 1").grid(column=0, row=0, padx=30, pady=10)
    ttk.Entry(tab2, textvariable=char1).grid(column=0, row=1, padx=30, pady=10)

    ttk.Label(tab2, text="Character 2").grid(column=1, row=0, padx=30, pady=10)
    ttk.Entry(tab2, textvariable=char2).grid(column=1, row=1, padx=30, pady=10)

    ttk.Label(tab2, text="Interaction on page: ").grid(
        column=0, row=2, padx=30, pady=10
    )
    ttk.Entry(tab2, textvariable=pageNum).grid(column=1, row=2, padx=30, pady=10)

    callFriendly = partial(createLink, char1, char2, "Friendly", pageNum, nodes, edges)
    callHostile = partial(createLink, char1, char2, "Hostile", pageNum, nodes, edges)
    ttk.Button(tab2, text="Create friendly link", command=callFriendly).grid(
        column=0, row=3, padx=30, pady=20
    )
    ttk.Button(tab2, text="Create hostile link", command=callHostile).grid(
        column=1, row=3, padx=30, pady=20
    )
    callSaveFile=partial(saveFile, nodes, edges, nodes_path, edges_path)
    ttk.Button(tab2, text="Save CSV file", command=callSaveFile).grid(
        column=0, row=4, padx=10, pady=10
    )

    # Populate character tab
    name = tk.StringVar()
    page = tk.StringVar()
    gender = tk.StringVar()

    ttk.Label(tab1, text="Character Name: ").grid(column=0, row=0, padx=10, pady=10)
    ttk.Entry(tab1, textvariable=name).grid(
        column=2, row=0, padx=10, pady=10
    )

    ttk.Label(tab1, text="Page first appear on: ").grid(
        column=0, row=1, padx=10, pady=10
    )
    ttk.Entry(tab1, textvariable=page).grid(
        column=2, row=1, padx=10, pady=10
    )

    ttk.Radiobutton(tab1, text="Male", variable=gender, value="M").grid(
        column=0, row=2, padx=20, pady=20
    )
    ttk.Radiobutton(tab1, text="Female", variable=gender, value="F").grid(
        column=1, row=2, padx=20, pady=20
    )
    ttk.Radiobutton(tab1, text="Unknown", variable=gender, value="").grid(
        column=2, row=2, padx=20, pady=20
    )

    callNewNode = partial(newNode, name, page, gender, nodes)
    ttk.Button(tab1, text="Add character", command=callNewNode).grid(
        column=0, row=3, padx=20, pady=20
    )

    callSaveFile=partial(saveFile, nodes, edges, nodes_path, edges_path)
    ttk.Button(tab1, text="Save CSV file", command=callSaveFile).grid(
        column=2, row=3, padx=20, pady=20
    )

    tabControl.pack(expand=1, fill="both")

    root.mainloop()