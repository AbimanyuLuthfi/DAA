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
graph_elements = { "T" : ["U", "W"],
                  "U" : ["T", "V"],
                  "V" : ["U", "X"],
                  "W" : ["T", "Z", "X"],
                  "X" : ["V", "S", "W"],
                  "Z" : ["W"],
                  "S" : ["X"]
                 }

g = graph(graph_elements)
g. addVertex("y")
print(g.getVertices())
