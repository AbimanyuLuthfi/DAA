import networkx as nx
import matplotlib.pyplot as plt

vertices = range (1,11)
edges = [(1,2), (1,7), (7,8), (7,9), (8,9), (7,10),
        (7,6), (6,2), (2,3), (3,6), (3,4), (6,5)]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
pos = nx.spring_layout(G)

nx.draw_networkx_nodes ( G, pos, nodelist = [1, 4, 3, 8, 9], label = True, node_color = 'g', node_size = 1300)

nx.draw_networkx_nodes ( G, pos, nodelist = [2, 5, 6, 7], label = True, node_color = 'r', node_size = 1300)

nx.draw_networkx_edges (G, pos, width = 3, alpha = 0.5, edge_color = 'b')
labels={}
labels[1]=r'1 NF'
labels[2]=r'2 F'
labels[3]=r'3 NF'
labels[4]=r'4 NF'
labels[5]=r'5 F'
labels[6]=r'6 F'
labels[7]=r'7 F'
labels[8]=r'8 NF'
labels[9]=r'9 NF'

nx.draw_networkx_labels(G,pos,labels,font_size=14)
