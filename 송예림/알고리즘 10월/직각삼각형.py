lst = []
while True:
    ex = list(map(int,input().split()))
    lst.append(ex)
    if len(ex)<=1:
        break

for i in range(len(lst)-1):
    one = lst[i]
    one.sort()
    if one[0]**2 + one[1]**2 == one[2]**2:
        print('rightangle')
    else:
        print('triangle')
