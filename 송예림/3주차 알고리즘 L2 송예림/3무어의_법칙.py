n = int(input())

num = 2**n

num_char =  str(num)
sum_list = []
for i in range(len(num_char)):
     sum_list.append(int(num_char[i]))

print(sum(sum_list))
