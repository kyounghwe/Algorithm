b_num =int(input())
b_work = str(input())
b_list = list(b_work.split(" "))
a_list = []
for i in range(0,b_num):
    if i == 0:
        a_list.insert(0,int(b_list[0]))
    else:
        a = (i+1)*int(b_list[i]) - (i)*int(b_list[i-1])
        a_list.append(a)
aa = [str (i) for i in a_list]

print(' '.join(s for s in aa))
