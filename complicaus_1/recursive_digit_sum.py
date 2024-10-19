# Source: HackerRank
# URL: https://www.hackerrank.com/challenges/recursive-digit-sum

def superDigit(n,k):
    x = k *sum(map(int,n))
    while x > 9:
        y=0
        while x>0:
            x,yp = divmod(x,10)
            y+= yp
        x=y
    return x