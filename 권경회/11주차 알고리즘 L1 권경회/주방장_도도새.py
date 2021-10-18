n, t = map(int, input().split())

takes_time = input().split()

res = []

for i in range(len(takes_time)):
    t -= int(takes_time[i])
    if t >= 0:
        res.append(t)

if len(res) >= len(takes_time):
    print(len(takes_time))
else:
    print(len(res))
