plus = list(map(str,input()))
num = len(plus)
f_n = ""
if num == 2:
    print(int(plus[0])+int(plus[1]))
else:
    n = plus[num-2:num]
    c = n[0]+n[1]
    if int(c) == 10:
        for i in range(num-2):
            f_n += plus[i]
        print(int(f_n)+10)
    else:
        for i in range(num-1):
            f_n += plus[i]
        print(int(f_n)+int(n[1]))
