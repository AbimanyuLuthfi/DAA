def bfs (graph, start) :
    visited = []
    queue = [start]
    
    while queue :
        node = queue.pop(0)
        if node not in visited :
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited
  
  graph = {'Amin' : {'Wasim', 'Nick', 'Mike'},
        'Wasim' : {'Imran', 'Amin'},
        'Imran' : {'Wasim', 'Faras'},
        'Faras' : {'Imran'},
        'Mike' : {'Amin'},
        'Nick' : {'Amin'}}
  
# O amin ------------------
# |              |          |
# O wasim       O nick     O mike  
# |
# O imran
# |
# O faras

bfs (graph, 'Amin')
