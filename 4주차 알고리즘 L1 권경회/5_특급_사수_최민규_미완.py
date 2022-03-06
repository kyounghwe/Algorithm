n = int(input())

count = 1

while 1:
    # 약수 개수
    cnt = 0
    for i in range(1, count + 1):
        if count % i == 0:
            cnt += 1

    if cnt > n:
        a = 1
        b = 1
        c = -2 * count
        r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
        if r1 >= 0 and r1 - int(r1) == 0:
            break
        else:
            count += 1
            continue
    else:
        count += 1

print(count)

'''
시간 초과로 수정 중.
'''
