# Source: HackerRank
# URL: https://www.hackerrank.com/challenges/breaking-best-and-worst-records

def breakingRecords(scores):
    broken_most = 0
    broken_last = 0
    max_score = scores[0]
    min_score = scores[0]
    
    for score in scores:
        if score > max_score:
            broken_most += 1
            max_score = score
            
        if score < min_score:
            broken_last += 1
            min_score = score
    
    return broken_most, broken_last