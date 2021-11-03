c,s,e = map(int,input().split())

real_c = c//2

stand = (c+s-e)//3 * 2

if stand >= c:
    print(real_c)
elif stand < c:
    print(stand//2)
else:
    print(0)
