N, T = map(int, input().split())
queue = list(map(int, input().split()))

cnt = 0
i = 0

if sum(queue)<T:
    print(N)

else:
    while T>0:
        T -= queue[i]

        if T < 0:
            break
        else:
            cnt += 1
    
    print(cnt)
