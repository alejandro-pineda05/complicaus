# Source: CSES
# URL: https://cses.fi/problemset/task/2428
# Solution by Pablo Reina Jimenez

n, k = map(int, input().split())
arr = list(map(int, input().split()))


count = {}
left = 0
result = 0
distinct_count = 0


for right in range(n):
    if arr[right] in count:
        count[arr[right]] += 1
    else:
        count[arr[right]] = 1
        distinct_count += 1

    while distinct_count > k:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
            distinct_count -= 1
        left += 1

    result += right - left + 1


print(result)
