t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().split())
    
    adjacency = [[] for _ in range(n+1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adjacency[u].append(v)
        adjacency[v].append(u)
    
    degrees = [len(adjacency[v]) for v in range(n+1)]
    
    leaves = {v for v in range(1, n+1) if degrees[v] == 1}
    
    center = None
    for v in range(1, n+1):
        if v not in leaves:
            if all(neigh not in leaves for neigh in adjacency[v]):
                center = v
                break
    
    x = degrees[center]
    # Cualquier vecino del centro sera un vertice intermedio
    mid_vertex = adjacency[center][0]
    y = degrees[mid_vertex] - 1
    
    print(x, y)
