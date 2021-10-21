n = input()

if len(n) == 4:
    a = n[:2]
    b = n[2:]
    print(int(a) + int(b))
elif n[-1] == '0':
    a = n[0]
    b = n[1:]
    print(int(a) + int(b))
else:
    a = n[:-1]
    b = n[-1]
    print(int(a) + int(b))
