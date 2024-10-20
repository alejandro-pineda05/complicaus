# Source: Codeforces Gym
# URL: https://codeforces.com/gym/102951/problem/A
# Solution by Kenny Jesús Flores Huamán

n = int(input())
x_coords = list(map(int, input().split()))
y_coords = list(map(int, input().split()))

def solve(n, x_coords, y_coords):
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            d = (x_coords[j] - x_coords[i])**2 + (y_coords[j]- y_coords[i])**2
            res = max(res, d)
    
    return res


print(solve(n, x_coords, y_coords))
