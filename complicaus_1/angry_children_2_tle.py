# Source: HackerRank
# URL: https://www.hackerrank.com/challenges/angry-children-2

def angryChildren(k, packets):
    packets.sort()

    unfairness = 0
    last_k = []
    for i in range(k):
        unfairness_i = 0
        for j in range(i+1, k):
            unfairness_i += abs(packets[i] - packets[j])
        last_k.append(unfairness_i)
        unfairness += unfairness_i
    mini = unfairness

    for i in range(k, len(packets)):
        unfairness -= last_k.pop(0)
        for j in range(1, k):
            unfairness_ij = abs(packets[i] - packets[i-j])
            last_k[-j] += unfairness_ij
            unfairness += unfairness_ij
        last_k.append(0)

        if unfairness < mini:
            mini = unfairness
