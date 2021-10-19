N = int(input())

blank = []

for i in range(1, N+1):
    blank.append(str(i))

num_string = ''.join(blank)

num = num_string.find(str(N))
print(num+1)
