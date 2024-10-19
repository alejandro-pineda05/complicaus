# Source: HackerRank
# URL: https://www.hackerrank.com/challenges/angry-children-2

def angryChildren(k, packets):
    packets.sort()

    unfairness = 0
    last_added = 0
    for i in range(1, k):
        last_added += i * (packets[i] - packets[i-1])
        unfairness += last_added
    mini = unfairness

    last_removed = 0
    for i in range(1, k):
        last_removed += packets[i] - packets[0]
    unfairness -= last_removed

    last_added = 0
    for i in range(1, k):
        last_added += packets[k] - packets[i]
    unfairness += last_added

    if unfairness < mini:
        mini = unfairness

    for i in range(1, len(packets) - k):
        last_removed += (
            - (k-1) * (packets[i] - packets[i - 1])
            + (packets[i+k - 1] - packets[i])
        )
        unfairness -= last_removed
        
        last_added += (
            + (k-1) * (packets[i+k] - packets[i+k - 1])
            - (packets[i+k - 1] - packets[i])
        )
        unfairness += last_added
        
        if unfairness < mini:
            mini = unfairness

    return mini
