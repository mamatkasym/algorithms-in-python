import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])
nx.draw_networkx(G)
plt.show()