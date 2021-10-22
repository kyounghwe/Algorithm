N = int(input())
num_list = list(map(int, input().split()))

new_list = []
new_list.append(num_list[0])
del num_list[0]

for new in new_list:
    for num in num_list:
        if (new+num)%3 != 0:
            new_list.append(num)
            num_list.remove(num)
        else:
            if (new_list[0]+num)%3 != 0:
                new_list.insert(0, num)
                num_list.remove(num)

if len(num_list) > 0:
    print(-1)
else:
    print(*(new_list))
