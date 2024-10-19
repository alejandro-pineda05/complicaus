# Source: HackerRank
# URL: https://www.hackerrank.com/challenges/birthday-cake-candles

def birthdayCakeCandles(candles):
    maxi = 0
    count = 0
    for candle in candles:
        if candle > maxi:
            maxi = candle
            count = 1
        elif candle == maxi:
            count += 1
    return count
