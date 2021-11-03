# 주문의 수 n, 도도새의 근무시간 t 입력
n, t = map(int, input().split())

# 각 주문을 처리하는 데 걸리는 시간을 주문 순서대로 입력
order = [int(o) for o in input().split()]

# 주문을 처리하는 데 소요된 시간
result = 0

# 처리한 주문 개수
cnt = 0

for o in order:
    result += o
    
    if (t - result) >= 0:
        cnt += 1
    else:
        break

print(cnt)

