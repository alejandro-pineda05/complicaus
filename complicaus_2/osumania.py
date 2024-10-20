# Source: Codeforces
# URL: https://codeforces.com/problemset/problem/2009/B
# Solution by Kenny Jesús Flores Huamán

t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    for _ in range(n):
        row = input()
        target = row.index('#') + 1

        res = [target] + res
    
    sol = ' '.join(map(str, res))
    print(sol)