# Source: HackerRank
# URL: https://www.hackerrank.com/challenges/apple-and-orange

def countApplesAndOranges(s, t, a, b, apples, oranges):
    res = 0
    for apple in apples:
        if s <= a+apple <=t:
            res += 1
    print(res)
    
    res = 0
    for orange in oranges:
        if s <= b+orange <=t:
            res += 1
    print(res)
