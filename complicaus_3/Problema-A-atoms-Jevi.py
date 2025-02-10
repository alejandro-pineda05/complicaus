valences = [int(x) for x in input().split()]

total = sum(valences)
if total % 2 != 0:
    print("Impossible")
    exit()

totalbonds = total // 2  # Total number of bonds between the atoms

bonds1 = valences[0]

remainder = totalbonds - bonds1  # The number of bonds between the other two atoms

twothree = remainder  # The number of bonds between atoms 2 and 3

threeone = valences[2] - twothree  # The number of bonds between atoms 3 and 1

onetwo = totalbonds - threeone - twothree  # The number of bonds between atoms 1 and 2

if onetwo + threeone != bonds1:
    print("Impossible")
    exit()

if any(x < 0 for x in [onetwo, threeone, twothree]):
    print("Impossible")
    exit()


print(onetwo, twothree, threeone)
