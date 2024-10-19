# Source: HackerRank
# URL: https://www.hackerrank.com/challenges/no-prefix-set/problem
# Solution by Pablo Reina Jimenez

def insert_word(trie, word):
    current = trie
    for char in word:
        if char not in current:
            current[char] = {}
        current = current[char]
        if "END" in current:
            return False

    current["END"] = True

    if len(current) > 1:
        return False

    return True


def check_good_set(words):
    trie = {}
    for word in words:
        if not insert_word(trie, word):
            print("BAD SET")
            print(word)
            return

    print("GOOD SET")


n = int(input())
words = [input().strip() for _ in range(n)]
check_good_set(words)
