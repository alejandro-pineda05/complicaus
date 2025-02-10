# Solution made by Jevi

from bisect import bisect_right

shops = int(input())
prices = sorted([int(x) for x in input().split()])
days = int(input())
coins = [int(input()) for _ in range(days)]

for day in range(days):
    c = coins[day]
    print(bisect_right(prices, c))
    
