n = input()
a = []

for i in range(0, len(n)):
    a.append(n[i])

# 스택 - 리스트에 하나씩 append 해주는데, 같은 문자가 들어오면 pop


def solution(s):
    res = []
    for i in range(0, len(a)):
        if len(res) > 0:
            if a[i] == res[len(res) - 1]:
                res.pop()
            else:
                res.append(a[i])
        else:
            res.append(a[i])
    return res


result = solution(n)

# 좌표 형식(?)으로 딕셔너리 만들기
new_list = []
for v in result:
    if v not in new_list:
        new_list.append(v)

dict = {}

for i in range(len(new_list)):
    s = new_list[i]
    index_arr = []
    for v in range(len(result)):
        if s == result[v]:
            index_arr.append(v)
    dict[s] = index_arr

# 겹치는 부분 경우의 수 구하기
cnt = 0

for i in range(len(dict)):
    rest = len(result) - dict[new_list[i]][1] - 1
    if rest > 0:
        for v in range(dict[new_list[i]][1] + 1, len(result)):
            if dict[result[v]][1] > dict[new_list[i]][1] and (dict[new_list[i]][0] < dict[result[v]][0] < dict[new_list[i]][1]):
                cnt += 1

print(cnt)
