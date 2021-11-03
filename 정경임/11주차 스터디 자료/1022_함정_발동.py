# 사람 위치
H = [input() for i in range(8)]
cnt = 0

for i in range(8): # 행
    for j in range(8):  # 열
        if i % 2 != 0 and j % 2 != 0 and H[i][j] == 'H':
            cnt += 1
        
        if i % 2 == 0 and j % 2 == 0 and H[i][j] == 'H':
            cnt += 1

print(cnt)
