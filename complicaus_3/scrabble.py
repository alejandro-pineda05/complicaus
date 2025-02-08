def solve(word:str) -> str:
    n = len(word)
    if n <= 10:
        return word
    
    res = word[0] + str(n-2) + word[-1]
    return res

n = int(input())

for _ in range(n):
    print(solve(input()))