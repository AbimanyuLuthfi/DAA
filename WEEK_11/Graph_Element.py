# a-----b
# /     /
# /     /
# c-----d-----e

# Create the dictionary with graph elements
graph = { "a" : ["b", "c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
        }

# Print the graph
print(graph)
