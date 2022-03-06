num = int(input())
num_list = []
for i in range(1, num):
    if i % 3 == 0 or i % 5 == 0:
        num_list.append(i)
print(sum(num_list))
