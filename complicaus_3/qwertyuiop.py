direction = input()
mole = input()

dicc = {}
rows = [
    "qwertyuiop",
    "asdfghjkl;",
    "zxcvbnm,./"
]

if direction == "R":
    for row in rows:
        n = len(row)
        dicc[row[0]] = row[0]
        for i in range(1,n):
            dicc[row[i]] = row[i-1]
else:
    for row in rows:
        n = len(row)
        dicc[row[-1]] = row[-1]
        for i in range(0,n-1):
            dicc[row[i]] = row[i+1]


w = [dicc.get(x) for x in mole]
print("".join(w))