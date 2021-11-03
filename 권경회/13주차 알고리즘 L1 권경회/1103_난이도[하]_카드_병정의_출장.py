n, m = map(int, input().split())

n_list = []

def num(x):
    if len(n_list) == m:
        print(' '.join(map(str, n_list)))
        return
        
    for i in range(x, n+1):
        if i not in n_list:
            n_list.append(i)
            num(i)
            n_list.pop()

num(1)
