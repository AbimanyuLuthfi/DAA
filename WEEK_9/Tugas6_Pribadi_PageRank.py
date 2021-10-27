# Tugas 6
myWeb = nx.DiGraph()
myPages = range(1,11)

connections = [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8), (8,9), (9,10), (10,11), (11,12), (12,1), (10,6), (6,2), (2,10), (12,4), (4,8), (8,12), (8,2), (12,6), (10,4)]
myWeb.add_nodes_from(myPages)
myWeb.add_edges_from(connections)

pos = nx.shell_layout(myWeb)
nx.draw(myWeb, pos, arrows = True, with_labels = True)
plt.show()

    nodes_set = len(aGraph)
    M = nx.to_numpy_matrix(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis = 1)))
    prob_outwards = np.array (
        [1.0/count
        if count > 0 else 0.0 for count in outwards])
    G = np.asarray(np.multiply(M.T, prob_outwards))
    p = np.ones(nodes_set) / float (nodes_set)
    if np.min(np.sum(G, axis = 0)) < 1.0 :
        print ('WARN : G is substochastic')
    return G,p

G, p = createPageRank(myWeb)
print (G)
