N = int(input())
Budget = list(map(int, input().split()))
M = int(input())

if sum(Budget) <= M:
    print(max(Budget))

else:
    M = M - min(Budget)
    Budget.remove(min(Budget))
    print(M//(N-1))
