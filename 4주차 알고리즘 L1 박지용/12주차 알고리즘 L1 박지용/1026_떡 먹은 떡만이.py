M = int(input())
rice_cake = [1,0,0]

for _ in range(M):
    a, b = map(int, input().split())
    temp = rice_cake[a-1]
    rice_cake[a-1] = rice_cake[b-1]
    rice_cake[b-1] = temp

for i in range(len(rice_cake)):
    if rice_cake[i]==1:
        print(i+1)
