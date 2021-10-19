order = list(map(int,input().split()))
times = list(map(int,input().split()))
num =0

for i in range(order[0]):
    if order[1]<times[i]:
        break
    else:
        num +=1
    order[1]-=times[i]

print(num)
