num = int(input())

if num > 1000:
    print(20)

elif num < 100:
    A = num//10
    B = num%10
    print(A+B)
else:
    if str(num)[1] == '0':
        A = num%10
        print(A+10)
    elif str(num)[2] == '0':
        A = num//100
        print(A+10)
