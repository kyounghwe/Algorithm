# 자연수 A와 B를 공백없이 입력
num_str = input()

result = 0  # 숫자의 합

# 입력받은 자연수 A, B가 한 자리 숫자라면
if len(num_str) == 2:
    result = int(num_str[0]) + int(num_str[1])

# 입력받은 자연수 A, B가 둘 중 하나라도 두 자리 숫자라면
else:
    # A가 10인 경우
    if num_str[1] == '0':
        ten = int(num_str[0:2])
        result = ten + int(num_str[2:])
    # B가 10인 경우
    else:
        ten = int(num_str[1:])
        result = int(num_str[0]) + ten
    
print(result)
