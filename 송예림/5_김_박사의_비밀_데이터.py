num = int(input())
num_list= []
for i in range(num):
    pw = int(input())
    num_list.append(pw)

num_sum = sum(num_list)
num_sum_list = str(num_sum)
print(num_sum_list[0:10])
