miro = []

for _ in range(8):
    miro.append(input())


cnt = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            if miro[i][j] == 'H':
                cnt +=1
        elif i % 2 == 1 and j % 2 == 1:
            if miro[i][j] == 'H':
                cnt +=1
print(cnt)
