# Source: HackerRank
# URL: https://www.hackerrank.com/challenges/largest-permutation/problem
# Solution by Pablo Reina Jimenez

def largestPermutation(k, arr):
    n = len(arr)
    index_map = {value: i for i, value in enumerate(arr)}
    for i in range(n):
        if k == 0:
            break
        max_val = n - i
        if arr[i] == max_val:
            continue
        max_val_index = index_map[max_val]
        arr[i], arr[max_val_index] = arr[max_val_index], arr[i]
        index_map[arr[max_val_index]] = max_val_index
        index_map[arr[i]] = i
        k -= 1
    return arr


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
result = largestPermutation(k, arr)
print(" ".join(map(str, result)))
