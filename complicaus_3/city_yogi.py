import math
from collections import deque

def build_capacity_matrix(w):
    cap_matrix = [[0]*(n) for _ in range(n)]
    
    if w > 0:
        for (u, v, cap) in edges:
            int_cap = int(cap // w)
            if int_cap > x:
                int_cap = x
            cap_matrix[u][v] = int_cap
    else:
        pass
    
    return cap_matrix

def edmond_karp(cap_matrix, s, t):
    flow = 0
    residual = [row[:] for row in cap_matrix]
    
    while True:
        parent = [-1]*n
        parent[s] = -2
        queue = deque()
        queue.append((s, math.inf))
        
        while queue and parent[t] == -1:
            u, f = queue.popleft()
            
            for v in range(n):
                if residual[u][v] > 0 and parent[v] == -1:
                    parent[v] = u
                    new_flow = min(f, residual[u][v])
                    if v == t:
                        flow += new_flow
                        cur = v
                        while cur != s:
                            prev = parent[cur]
                            residual[prev][cur] -= new_flow
                            residual[cur][prev] += new_flow
                            cur = prev
                        break
                    queue.append((v, new_flow))
        
        if parent[t] == -1:
            break
    
    return flow



n, m, x = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))


max_capacity = max(c for _, _, c in edges)



lo, hi = 0.0, float(max_capacity)
EPS = 1e-7

for _ in range(60):
    mid = (lo + hi) / 2.0
    cap_matrix = build_capacity_matrix(mid)
    f = edmond_karp(cap_matrix, 0, n - 1)
    
    if f >= x:
        lo = mid
    else:
        hi = mid

answer = x * lo
print(f"{answer:.9f}")
