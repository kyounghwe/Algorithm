n = str(input())

a = "1"

for i in range(2, int(n)+1):
    a += str(i)

print(a.find(n)+1)
