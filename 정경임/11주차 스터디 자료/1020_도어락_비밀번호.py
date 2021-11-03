# 체셔 고양이와 엘리스가 태어난 년도인 자연수 N1,N2를 입력
n1, n2 = input().split()

# 태어난 연도의 모든 자릿수를 역순으로 바꾸어 수를 얻기
reversed_n1 = n1[::-1]
reversed_n2 = n2[::-1]

# 역순의 숫자 더하기
result = int(reversed_n1) + int(reversed_n2)

print(result)
