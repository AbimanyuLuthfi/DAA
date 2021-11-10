# Latihan 2 
class graph :
    def __init__(self,gdict = None) :
        if gdict is None :
            gdict = []
        self.gdict = gdict

# Get the keys of the dicionary
    def getVertices(self) :
        return list(self.gdict.keys())
        
# Create the dictionary with graph elements
graph_elements = {"R" : ["L", "O"],
                 "O" : ["R", "M", "P"],
                 "M" : ["N", "O"],
                 "L" : ["R", "P"],
                 "P" : ["L", "N", "O"],
                 "N" : ["M", "P"]
                 }
g = graph(graph_elements)
print(g.getVertices())
