def dfs (graph, start, visited = None) :
    if visited is None :
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited :
        dfs(graph, next, visited)
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
# turun dari amin ke faras, geser ke nick & mike

dfs (graph, 'Amin')
