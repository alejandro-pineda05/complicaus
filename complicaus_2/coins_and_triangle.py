# Source: CodeChef
# URL: https://www.codechef.com/problems/TRICOIN
# Solution by Kenny Jesús Flores Huamán

import math

def solve(n):   
    return int((-1 + math.sqrt(1 + 8 * n)) // 2)

if __name__ == "__main__":
    tests = int(input()) 
    for _ in range(tests):
        n = int(input()) 
        print(solve(n))