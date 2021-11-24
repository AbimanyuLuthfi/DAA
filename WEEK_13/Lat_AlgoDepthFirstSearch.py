# Latihan Algoritma DFS
def dfs (graph, start, visited = None) :
    if visited is None :
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited :
        dfs(graph, next, visited)
    return visited
  
  graph = {'Rektor' : {'Warek 1', 'Warek 2'},
        'Warek 1' : {'Rektor'},
        'Warek 2' : {'Kaprodi 1', 'Kaprodi 2', 'Kaprodi 3', 'Rektor'},
        'Kaprodi 1' : {'Dosen A','Dosen B','Dosen C', 'Warek 2'},
        'Kaprodi 2' : {'Dosen D', 'Dosen E', 'Warek 2'},
        'Kaprodi 3' : {'Dosen F', 'Dosen G', 'Warek 2'},
        'Dosen A' : {'Kaprodi 1'},
        'Dosen B' : {'Kaprodi 1'},
        'Dosen C' : {'Kaprodi 1'},
        'Dosen D' : {'Kaprodi 2'},
        'Dosen E' : {'Kaprodi 2'},
        'Dosen F' : {'Kaprodi 3'},
        'Dosen G' : {'Kaprodi 3'}
        }

dfs (graph, 'Rektor')
