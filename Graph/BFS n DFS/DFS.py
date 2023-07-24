def DFS(graph, vis, node):
    if node not in vis:
        print(node, end =" ")
        vis.add(node)

        for neighbour in graph[node]:
            DFS(graph, vis, neighbour)

    
if __name__ == "__main__":
    
    graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
    }

    vis =set()
    
    DFS(graph, vis, '5')