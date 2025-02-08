import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, s):
        node = self.root
        for c in s:
            if c not in node:
                node[c] = {}
            node = node[c]

        if self.end_symbol not in node:
            node[self.end_symbol] = 0
        node[self.end_symbol] += 1

    def search(self, s):
        node = self.root
        for c in s:
            if c not in node:
                return 0
            node = node[c]

        if self.end_symbol in node:
            return node[self.end_symbol]
        else:
            return 0

def solve(sentence: str, trie: Trie) -> int:
    acc = 1 
    for s in sentence:
        if len(s) <= 3:
            acc *= trie.search(s) 
        else:

            s_encoding = s[0] + ''.join(sorted(s[1:-1])) + s[-1]
            acc *= trie.search(s_encoding) 
    return acc

T = int(input())
for i in range(T):
    trie = Trie()
    n = int(input())
    for _ in range(n):
        word = input().strip()
        if len(word) <= 3:
            word_encoding = word
        else:
            word_encoding = word[0] + ''.join(sorted(word[1:-1])) + word[-1]
        trie.add(word_encoding) 

    print(f"Case {i + 1}:")
    m = int(input()) 
    for _ in range(m):
        sentence = input().strip().split() 
        print(solve(sentence, trie)) 