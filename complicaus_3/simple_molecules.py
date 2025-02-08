a, b, c = map(int, input().split())

if (a + b + c) % 2 != 0:
    print("Impossible")
else:
    x = (a + b - c) // 2
    y = (b + c - a) // 2
    z = (c + a - b) // 2
    if x < 0 or y < 0 or z < 0:
        print("Impossible")
    else:
        print(x, y, z)