x = input()

def decom(x):
    # 문자열에서 ')' 삭제
    x = x.replace(")", "")

    # 문자열에서 '(' 있는 지 확인
    b = x.find('(')
    
    # 문자열에서 '(' 없을 때 x의 길이 반환
    if b == -1:
        return len(x)
    # 문자열에서 '(' 있을 때

    else:
        # 문자열의 뒤에서 두번째 인덱스부터 하나씩 확인
        for i in range(len(x)-1, -1, -1):
            if x[i] == "(":
                # i가 '(' 일때 '(' 앞을 int, 뒤를 str 둘이 곱해주고
                n = int(x[i-1]) * x[i+1:]
                # x를 '(' 앞 인덱스까지 자르고 곱한 값을 뒤에 더해줌
                x = x[:i-1] + n
                return decom(x)

print(decom(x))
