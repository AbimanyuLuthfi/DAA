# Latihan 2
import networkx as nx
import matplotlib.pyplot as plt
vertices = range(1,15)
edges = [(9,6), (7,6), (14,6), (8,6), (6,2), (11,2), (12,2), (15,2), (2,1), (4,1), (10,1), (2,3), (13,3), (5,3)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels = True, node_color = 'g', node_size = 1000)

nx.degree_centrality(G)
nx.betweenness_centrality(G)
nx.closeness_centrality(G)
centrality = nx.eigenvector_centrality(G)
sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())
