nickname = input()
n = int(input())
string = [input() for _ in range(n)]

cnt = 0

for i in string:
    cnt += i.count(nickname)
    for j in range(-len(nickname)+1, 0):
        m = j + len(nickname)
        print(j)
        print(m)
nickname = input()
n = int(input())
string = [input() for _ in range(n)]

cnt = 0

for i in string:
    cnt += i.count(nickname)

    # 시작과 끝이 포함된 글자(별명의 길이만큼)의 경우와 별명이 같은 지
    for j in range(-len(nickname)+1, 0):
        m = j + len(nickname)
        if (i[j:] + i[:m]) == nickname:
            cnt += 1

print(cnt)


# 60점.. 오답의 케이스를 모르겠음.
