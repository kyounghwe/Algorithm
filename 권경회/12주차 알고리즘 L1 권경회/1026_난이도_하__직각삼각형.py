tr = []

for i in range(3):

    t = list(map(int, input().split()))

    if t[0] == 0:
        break
    else:
        tr.append(t)

for j in tr:
    j.sort()
    if (j[0] ** 2) + (j[1] ** 2) == j[-1] ** 2:
        print("rightangle")
    else:
        print("triangle")
