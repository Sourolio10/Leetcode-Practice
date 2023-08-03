
def BFS(graph, vis, q, node):
    vis.append(node)
    q.append(node)
    res =[]
    while q:
        m = q.pop(0)
        print(m, end= " ")

        for neighbour in graph[m]:
            if neighbour not in vis:
                vis.append(neighbour)
                q.append(neighbour)

    
if __name__ == "__main__":
    
    graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
    }

    vis =[]
    q =[]
    BFS(graph, vis, q, '5')