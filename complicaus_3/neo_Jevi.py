# Solution made by Jevi

moves = 0
for h in [1, 2, 3, 4, 5]:
    line = input().split()
    if "1" in line:
        moves += abs(h-3)
        moves += abs(line.index("1") - 2)
        break

print(moves)
