birth = list(map(str,input().split()))
one = birth[0]
two = birth[1]

a = int(one[::-1])
b = int(two[::-1])

print(a+b)
