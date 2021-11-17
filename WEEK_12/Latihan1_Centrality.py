# Latihan 1
import networkx as nx
import matplotlib.pyplot as plt

edges = [('Bob', 'Mike'), ('Mike', 'Emma'), ('Bob', 'John'), ('John', 'Leah'), ('Leah', 'Shane'), ('Shane', 'Emma'), ('Emma', 'Mike'), ('Mike', 'Jill'), ('Bob', 'Jill'), ('Jill', 'John'), ('Jill', 'Leah'), ('Jill', 'Shane'), ('Jill', 'Emma'), ('John', 'Shane'), ('Bob', 'Emma'), ('Emma', 'Liz'), ('Shane', 'Liz'), ('Liz', 'Allen'), ('Allen', 'Lisa')]
G = nx.Graph()

G.add_edges_from(edges)
nx.draw(G, with_labels = True, node_color = 'y', node_size = 1000)

nx.degree_centrality(G)
nx.betweenness_centrality(G)
nx.closeness_centrality(G)
centrality = nx.eigenvector_centrality(G)
sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())
