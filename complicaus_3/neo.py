n = 5 # 5x5

matrix = []

for _ in range(n):
    ls = list(map(int,input().split()))
    matrix.append(ls)


for row in range(n):
    for col in range(n):
        if matrix[row][col] == 1:
            x1 = row+1
            y1 = col+1
            res = abs(x1-3) + abs(y1-3)
            print(res)
            break