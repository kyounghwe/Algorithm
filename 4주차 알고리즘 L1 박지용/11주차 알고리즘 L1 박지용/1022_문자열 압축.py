def decompress(S):
    if len(S) == 5:
        return 1 + (len(S[3]) * int(S[1]))
    
    return (int(S[1]) * decompress(S[3:-1])) + 1
    
S = input()
print(decompress(S))

#제출결과 : 20점
#나머지 TestCase에서 valueError가 나옴..
#아마도 입력에서 11(18(72(7)))의 형식이 아닌
#4(18(72(7)))처럼 한자리가 입력 될 수도 있을 거라고 예상됨...
