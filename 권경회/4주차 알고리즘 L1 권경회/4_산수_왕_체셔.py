a, b, c = map(int, input().split())

# b를 2진수로 변환 후 리스트에 담고 뒤집기
B = bin(b)

i_list = []
for i in B[2:]:
    i_list.append(i)

r_i_list = i_list[::-1]

# 2진수로 바꾼 b를 2의 거듭제곱으로 변환 후 리스트에 넣기
s_list = []

for s in range(len(r_i_list)):
    if i == 0:
        x = 1 if r_i_list[int(s)] == "1" else 0
        s_list.append(x)
    else:
        if r_i_list[s] == "1":
            t = 2 ** s
            s_list.append(t)

# 2 ≤ B 인 거듭제곱의 c로 나눈 나머지 구함.
sq_list = []

for z in range(len(s_list)):
    sq = a ** int(s_list[z]) % c
    sq_list.append(sq)

# 나머지들을 곱한 후 c로 나눈 나머지를 구함.
po = 1

for k in sq_list:
    po *= k

print(po % c)


'''

https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation 방법 -> 시간 초과

'''
