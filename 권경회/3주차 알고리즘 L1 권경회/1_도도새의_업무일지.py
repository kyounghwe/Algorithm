n = int(input())
b_num = input().split()

a_list = []

for i in range(0, n):
    if i == 0:
        a_list.append(int(b_num[0]))
    else:
        a_value = (int(b_num[i]) * (i+1)) - (int(b_num[i-1]) * i)
        a_list.append(a_value)

for a in a_list:
    print(a, end=' ')
