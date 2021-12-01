import networkx as nx
import matplotlib.pyplot as plt

vertices = range (1,10)
edges = [(7,2), (2,3), (7,4), (4,5), (7,3), (7,5),
        (1,6), (1,7), (2,8), (2,9)]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
pos = nx.spring_layout(G)

nx.draw_networkx_nodes ( G, pos,
                        nodelist = [1, 4, 3, 8, 9],
                        label = True,
                        node_color = 'g',
                        node_size = 1300)
