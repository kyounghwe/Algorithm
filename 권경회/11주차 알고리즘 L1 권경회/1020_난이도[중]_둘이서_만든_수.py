T = int(input())
N = int(input())
A = [int(i) for i in input().split()]
M = int(input())
B = [int(i) for i in input().split()]


def number_of_cases(x):
    sum_list = []
    ay_len = len(x)
    for i in range(ay_len):
        sum_list.append([x[i]])

    for i in range(ay_len-1):
        for j in range(1, ay_len):
            a = x[i] + x[j]
            if i >= j:
                continue

            if i + 1 == j:
                q = [x[i], x[j]]
                if a < T:
                    sum_list.append(q)

    sum_list_sum = []
    for i in sum_list:
        w = sum(i)
        sum_list_sum.append(w)

    return sum_list_sum


A_case = number_of_cases(A)
B_case = number_of_cases(B)
cnt = 0

for i in A_case:
    for j in B_case:
        if i + j == T:
            cnt += 1

print(cnt)
