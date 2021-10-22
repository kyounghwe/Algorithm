N = int(input())
num_list = list(map(int, input().split()))


lt=0
rt=1
temp = 0
while True:
    if rt < len(num_list)-1:
        if (num_list[lt]+num_list[rt]) % 3 == 0:
            temp = num_list[rt]
            num_list[rt] = num_list[rt+1]
            num_list[rt+1] = temp
            rt +=1
            lt +=1
        else:
            rt+=1
            lt+=1
    else:
        break

print(*(num_list))
