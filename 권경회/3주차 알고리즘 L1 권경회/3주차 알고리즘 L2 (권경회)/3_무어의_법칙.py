n = int(input())

moore = str(2 ** n)

moore_list = []

for i in moore:
    i = int(i)
    moore_list.append(i)

print(sum(moore_list))
