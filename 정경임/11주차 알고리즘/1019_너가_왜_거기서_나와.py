n = input()

# 이어질 숫자
num = ''

for i in range(1, int(n)+1):
    num += str(i)
    
print(num.find(n) + 1)  # 0부터 시작하기 때문에 1 더해주기


'''
<< 문자열에서 문자 위치 찾기 >>
-- num : 문자열, n : 찾을 문자

1. find()
    발견된 문자의 첫 번째 위치 반환
    찾을 문자가 발견되지 않으면 -1 반환
    ex.num.find(n)
    
2. rfind()
    하위 문자열의 마지막 위치를 반환. 뒤에서부터 검색해서 발견된 위치 반환
    ex.num.rfind(n)
    
3. index()
    발견된 문자의 첫 번째 위치 반환
    찾을 문자가 발견되지 않으면 ValueError 반환
    ex.num.index(n)
    
4. for문, enumerate()
    문자열에 있는 모든 문자를 개별적으로 확인.
    일치하는 모든 위치가 표시되고 다른 변수에 저장    
    ex1.result = []
        for a, b in enumerate(num):
            if b == n:
                result.append(a)
        print(result)
    ex2.print([a for a, b in enumerate(num) if b == n])
'''
