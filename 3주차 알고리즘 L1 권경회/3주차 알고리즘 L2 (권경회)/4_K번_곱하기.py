n, k = map(int, input().split())

sum_list = []

for i in range(1, n+1):
    i = i ** k
    sum_list.append(i)

result = sum(sum_list) % 1000000009

print(result)
