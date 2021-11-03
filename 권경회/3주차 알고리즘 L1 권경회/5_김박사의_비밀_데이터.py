n = int(input())
a = []

for i in range(0, n):
    i = int(input())
    a.append(i)

b = str(sum(a))
print(b[0:10])
