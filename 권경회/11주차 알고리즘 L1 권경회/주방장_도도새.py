n, t = map(int, input().split())

takes_time = input().split()

time_list = []

for i in takes_time:
    t = t - int(i)
    time_list.append(t)

for i in range(len(time_list)):
    if time_list[-1] > 0:
        print(len(time_list))
        break

    if time_list[i] <= 0:
        print(len(time_list[:i]))
        break
