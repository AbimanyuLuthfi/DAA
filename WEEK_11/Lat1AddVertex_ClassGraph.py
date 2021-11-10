# Latihan 1
class graph :
    
    def __init__(self,gdict = None) :
        if gdict is None :
            gdict = {}
        self.gdict = gdict
        
    def getVertices(self) :
        return list(self.gdict.keys())
    
# Add the vertex as a key
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

# Create the dictionary with graph elements
graph_elements = {"R" : ["L", "O"],
                 "O" : ["R", "M", "P"],
                 "M" : ["N", "O"],
                 "L" : ["R", "P"],
                 "P" : ["L", "N", "O"],
                 "N" : ["M", "P"]
                 }

g = graph(graph_elements)
g. addVertex("o")
g. addVertex("p")
print(g.getVertices())
