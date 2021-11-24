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
# naik nicks ke amin, turun ke faras, geser ke mike

dfs (graph, 'Nick')
