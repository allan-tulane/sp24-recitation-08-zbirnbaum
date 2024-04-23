from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    visited = {}
    visited[source] = (0,0)
    queue = deque([source])
    while queue:
      node = queue.popleft()
      for neighbor, weight in graph[node]:
        if neighbor not in visited:
          visited[neighbor] = (visited[node][0] + weight, visited[node][1] + 1)
          queue.append(neighbor)
    return visited
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    visited = {}
    visited[source] = None
    queue = deque([source])
    while queue:
      node = queue.popleft()
      for neighbor in graph[node]:
        if neighbor not in visited:
          visited[neighbor] = node
          queue.append(neighbor)
    return visited
    

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path, as a string, from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example:
  """
    path = []
    curr = destination
    if destination in parents:
      curr = parents[destination]

    while curr is not None and curr != destination:
      path.append(curr)
      curr = parents[curr]

    path.reverse()
  
    path_string = ""
    for node in path:
      path_string += node
    
    return path_string
    
    
      
    
      
    
    
    

