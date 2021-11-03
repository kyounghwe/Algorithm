n = int(input())
n_list = list(map(int,input().split()))

lt=0
rt=1
temp = 0
while True:
    if rt < len(n_list)-1:
        if (n_list[lt]+n_list[rt]) % 3 == 0:
            temp = n_list[rt]
            n_list[rt] = n_list[rt+1]
            n_list[rt+1] = temp
            rt +=1
            lt +=1
        else:
            rt+=1
            lt+=1
    else:
        break

print(*(n_list))
