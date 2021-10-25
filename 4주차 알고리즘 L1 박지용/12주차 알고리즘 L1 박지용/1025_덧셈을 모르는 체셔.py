num = int(input())

if num > 1000:
    print(20)
elif num > 100:
    if str(num)[1] == '0':
        print(10+num%10)
    else:
        print(10+num//100)
else:
    print(num//10 + num%10)
