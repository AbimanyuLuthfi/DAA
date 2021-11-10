# Latihan 1
# Create the dictionary with graph elements
graph = { "T" : ["U", "W"],
          "U" : ["T", "V"],
          "V" : ["U", "X"],
          "W" : ["T", "Z", "X"],
          "X" : ["V", "S", "W"],
          "Z" : ["W"],
          "S" : ["X"]
        }

# Print the graph
print(graph)
