# Latihan 1
class graph :
    
    def __init__(self,gdict = None) :
        if gdict is None :
            gdict = {}
        self.gdict = gdict
        
    def edges(self) :
        return self.findedges()
    
# Find the disctinct list of edges
    def findedges(self) :
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if{nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    
# Create the dictionary with graph elements
graph_elements = { "T" : ["U", "W"],
                  "U" : ["T", "V"],
                  "V" : ["U", "X"],
                  "W" : ["T", "Z", "X"],
                  "X" : ["V", "S", "W"],
                  "Z" : ["W"],
                  "S" : ["X"]
                 }
g = graph(graph_elements)
print(g.edges())
