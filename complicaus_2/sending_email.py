# Source: UVA
# URL: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1927
# Solution by Pablo Reina Jimenez

import heapq


def find_shortest_time(n, m, s, t, connections):
    graph = [[] for _ in range(n)]
    for u, v, w in connections:
        graph[u].append((w, v))
        graph[v].append((w, u))

    distances = [float('inf')] * n
    distances[s] = 0
    pq = [(0, s)]

    while pq:
        current_distance, u = heapq.heappop(pq)
        if u == t:
            return current_distance
        if current_distance > distances[u]:
            continue
        for weight, v in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))

    return 'unreachable'


N = int(input())
for case in range(1, N + 1):
    n, m, S, T = map(int, input().split())
    connections = [tuple(map(int, input().split())) for _ in range(m)]
    result = find_shortest_time(n, m, S, T, connections)
    print(f'Case #{case}: {result}')
