t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))

    max_length = 0
    current_sum = 0
    start = 0

    for end in range(n):
        if end > 0 and h[end - 1] % h[end] != 0:
            start = end
            current_sum = 0

        current_sum += a[end]

        while current_sum > k:
            current_sum -= a[start]
            start += 1

        max_length = max(max_length, end - start + 1)

    print(max_length)