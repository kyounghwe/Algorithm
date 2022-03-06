a, b, c = map(int, input().split())

result = 1

# 지수가 1이 될 때 무조건 결과값에 곱하게 되어있으므로 0이 될 때까지 계속한다.
while b:
    # 홀수일 경우를 따로 빼서 결과값에 밑을 한번 곱해준다.
    if int(b) & 1:
        result = (result * a) % c

    # 짝수/홀수 상관없이 밑을 제곱한다. 그리고 지수를 반으로 쪼갠다.
    a = (a ** 2) % c
    b /= 2


print(result)

'''
https://sexycoder.tistory.com/68 

거듭제곱의 분할 정복

'''
