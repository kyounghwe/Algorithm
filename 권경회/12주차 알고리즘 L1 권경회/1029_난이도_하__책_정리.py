n = int(input())
x = input().split()
t = list(map(int, x))


def lower(t, a):
    for i in range(len(t)):
        if (t[i] < a) and (a < t[i+1]):
            return i+1
        if t[i] == a:
            return i


ans = [0]

for i in range(n):
    if ans[len(ans)-1] < t[i]:
        ans.append(t[i])
    else:
        pos = lower(ans, t[i])
        ans[pos] = t[i]

print(n - len(ans) + 1)
