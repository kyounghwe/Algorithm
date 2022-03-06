n, m = map(int, input().split())

n_list = []

# 재귀
def num():
    if len(n_list) == m:
        print(' '.join(map(str, n_list)))
        return
     
    for i in range(1, n+1):
        n_list.append(i)
        num()
        n_list.pop()

num()

