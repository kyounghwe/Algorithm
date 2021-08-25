s = input()
t = input()

s_string = ''
t_string = ''

result = 0
# s 문자열의 길이가 50을 초과 할 때 까지 추가
while len(s_string) < 50:
    s_string += s

# t 문자열의 길이가 50을 초과 할 때 까지 추가
while len(t_string) < 50:
    t_string += t

#두 문자열의 인덱스 하나 하나씩 비교
for i in range(0, 50):
    if(s_string[i] == t_string[i]):
        result = 1
        continue
    else:
        result = 0
        break

print(result)
