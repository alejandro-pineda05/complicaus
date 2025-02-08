import math
t = int(input())

def solve(weights, W):
    min_weight = math.ceil(W/2)

    for i, c in enumerate(weights):
        if (c >= min_weight) and (c<=W):
            print(1)
            print(i+1)
            return
        
    subset = []
    total_weight = 0
    weights_sorted = sorted(enumerate(weights), key=lambda x:x[1], reverse=True)
    for i,w in weights_sorted:
        if w <= W:
            subset.append(i+1)
            total_weight+=w
            if total_weight >= min_weight:
                print(len(subset))
                print(*subset)
                return 


    # Si no se consigue solución, se imprime -1
    print(-1)
    return

for _ in range(t):
    n, W = map(int, input().split()) # Número de objetos, W= capacidad máxima
    weights = list(map(int,input().split()))
    solve(weights, W)
