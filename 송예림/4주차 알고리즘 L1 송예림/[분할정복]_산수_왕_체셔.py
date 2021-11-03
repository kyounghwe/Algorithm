A, B, C = map(int, input().split())

multi_form = []
while True:
    if B == 1: 
        break
    if B % 2 == 0: 
        multi_form.append(False)
    else: 
        multi_form.append(True)
    B = B // 2

# 자주 쓰이는 연산이니 따로 변수로 저장
D = A % C
result = D
for form in multi_form[::-1]:
    if form: 
        result = result ** 2 * (D)
    else: 
        result = result ** 2
    result = result % C

print(result)

#백준 코딩 참고하였습니다
