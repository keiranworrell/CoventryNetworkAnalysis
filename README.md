# CoventryNetworkAnalysis
## Author: Keiran Worrell, 7872855
This repository is a collection of the scripts created throughout the final year Mathematics project (331MP) of Keiran Worrell. The project is on the topic of network analysis on the book *Shaka Zulu: The Rise of The Zulu Empire* by E. A. Ritter.

Some of the scripts included in this repository are tailored for use with a network of this book, for example networkAnalysis/giant_stability.py contains some character names. If these scripts are to be used in the analysis of any other texts, the specifics for *Shaka Zulu* must first be removed.

We have included two main pieces of functionality in this repository - one for collection of data, and one for the analysis of data. The main.py script will, when run, request that the user chooses between these functions and will then launch the requested one.

### Data Collection

If the data collection functionality is chosen, a user interface is launched which should be used while reading and extracting data from a text.

This interface allows for recording of characters as nodes and their interactions as edges between these nodes, to form a social network representing the text.

The nodes can be recorded with extra information, such as gender of a character and when they are introduced, and the edges can be classified as either friendly or hostile, while recording the page on which the interaction occurs.

Nodes and edges are saved to csv files in a location of the user's choice, and are formatted in a way that allows them ot then be used in Gephi to visualise the network and extract data. 

### Data Analysis

The data analysis segment of the code extracts the network data from the .csv files in which the data collection scripts saved it. It then conducts various pieces of data analsis and outputs the results to the console.

This functionality is the most customised to analysing *Shaka Zulu*, for example creating a duplicate set of network data without the main character Shaka. This can be altered though.

The code is structured in a way that should make it easy to customise the data extracted from the network. In networkAnalysis/graph.py, various other functions are imported then called to extract information from the network.

### Other Scripts
Outside of these two main pieces of functionality, we have included two additional scripts.

randomGraph.py generates random graphs with the same average degree as the one being analysed, but requires the number of nodes and the mean degree to be altered before use.

degdist.py generates a series of plots of the degree distribution of the network, but before use the degrees and their frequencies must be updated.
