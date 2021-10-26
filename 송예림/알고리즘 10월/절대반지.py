hat = str(input())
dodo = int(input())
ring = []
for i in range(dodo):
    ring.append(str(input()))

cnt = 0
anw1 = []
anw2 = []

for i in range(len(ring)):
    lst = ring[i]
    if hat in lst:
        anw1.append(lst)
    else:
        new = lst[-(len(hat)):]+lst[:len(hat)-1]
        if hat in new:
            anw2.append(new)

r1 = set(anw1)
r2 = set(anw2)

print(len(r2)+len(r1))
