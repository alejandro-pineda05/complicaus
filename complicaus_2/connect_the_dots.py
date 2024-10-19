# Source: CodeForces
# URL: https://codeforces.com/problemset/problem/2020/D
# Solution by Pablo Reina Jimenez

def find_par(a, par):
    if par[a] == a:
        return a
    par[a] = find_par(par[a], par)
    return par[a]


def unite(a, b, par, sz):
    a = find_par(a, par)
    b = find_par(b, par)
    if a == b:
        return
    if sz[b] > sz[a]:
        a, b = b, a
    sz[a] += sz[b]
    par[b] = a


def solve():
    n, m = map(int, input().split())
    C = 11

    par = list(range(n + 1))
    sz = [1] * (n + 1)
    dp = [[0] * C for _ in range(n + 1)]
    ind = [[i] * C for i in range(n + 1)]
    start_cnt = [[0] * C for _ in range(n + 1)]
    end_cnt = [[0] * C for _ in range(n + 1)]

    for _ in range(m):
        a, d, k = map(int, input().split())
        if a <= n:
            start_cnt[a][d] += 1
        if a + k * d <= n:
            end_cnt[a + k * d][d] += 1

    for i in range(1, n + 1):
        for j in range(1, C):
            dp[i][j] = start_cnt[i][j] - end_cnt[i][j]
            if i - j < 1:
                continue
            if dp[i - j][j] > 0:
                unite(ind[i - j][j], i, par, sz)
                ind[i][j] = ind[i - j][j]
                dp[i][j] += dp[i - j][j]

    ans = sum(1 for i in range(1, n + 1) if find_par(i, par) == i)
    print(ans)


t = int(input())
for _ in range(t):
    solve()
