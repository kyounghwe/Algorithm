n = [input() for _ in range(8)]

cnt = 0

for i in range(8):
    for j in range(8):
        if i % 2 != 0 and j % 2 != 0:
            if n[i][j] == 'H':
                cnt += 1
        if i % 2 == 0 and j % 2 == 0:
            if n[i][j] == 'H':
                cnt += 1
print(cnt)
