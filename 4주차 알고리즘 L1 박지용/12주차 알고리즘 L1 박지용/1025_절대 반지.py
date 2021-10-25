Nickname = input()
N = int(input())

ring_string = []
for _ in range(N):
    ring_string.append(input())

#print(ring_string)

cnt = 0
for string in ring_string:
    if Nickname in string:
        cnt += 1

print(cnt)

#별명이 ABC일 때, CWEQWFGAB의 문자열일 경우를 고려하지 않음....
#60점 
