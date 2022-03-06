m = int(input())

r = []

c = ['A', 'B', 'C']

for i in range(m):
    a, b = map(int, input().split())
    r.append((a, b))

for i in range(m):
    t = c[r[i][0]-1]
    c[r[i][0]-1] = c[r[i][1]-1]
    c[r[i][1]-1] = t

print(c.index('A')+1)
