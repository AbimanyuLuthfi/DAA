def createPageRank(aGraph) :
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
