# Some test code with networkx
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

    G.add_node('santaclaus')
    G.add_nodes_from([1, 'superman', 'robin hood'])

    G.add_edge('santaclaus', 'superman')
    G.add_edge('santaclaus', 'robin hood')

    nx.draw(G)
# plt.savefig("simple_path.png")
     plt.show()

     print(G.nodes())
     print(G.edges())

     print(type(G.nodes()))
     print(type(G.edges()))
