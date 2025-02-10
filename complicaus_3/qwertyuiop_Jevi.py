# Solution made by Jevi

first = list("qwertyuiop")
second = list("asdfghjkl;")
third = list("zxcvbnm,./")

LEFT = {x: first[i-1] for i, x in enumerate(first, start=0) if i != 0}
LEFT[first[0]] = first[0]
LEFT.update({x: second[i-1] for i, x in enumerate(second, start=0) if i != 0})
LEFT[second[0]] = second[0]
LEFT.update({x: third[i-1] for i, x in enumerate(third, start=0) if i != 0})
LEFT[third[0]] = third[0]

RIGHT = {x: first[i] for i, x in enumerate(first, start=1) if i != len(first)}
RIGHT[first[-1]] = first[-1]
RIGHT.update({x: second[i] for i, x in enumerate(second, start=1) if i != len(second)})
RIGHT[second[-1]] = second[-1]
RIGHT.update({x: third[i] for i, x in enumerate(third, start=1) if i != len(third)})
RIGHT[third[-1]] = third[-1]


shift = input()
dictionary = LEFT if shift == "R" else RIGHT

chars = input()
new = ""
for ch in chars:
    new += dictionary[ch]

print(new)
