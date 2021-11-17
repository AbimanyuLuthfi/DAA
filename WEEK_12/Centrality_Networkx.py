# Install Networkx terlebih dahulu
pip install networkx

# Import Networkx dan Matplotlib
import networkx as nx
import matplotlib.pyplot as plt

# Tentukan Vertices
vertices = range(1,10)

# Tentukan Hubungan Antara Edges Sesuai Vertices yang sudah ditentukan
edges = [(7,2), (2,3), (7,4), (4,5), (7,3), (7,5), (1,6), (1,7), (2,8), (2,9)]

# Mencetak Edges
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels = True, node_color = 'y', node_size = 800)
