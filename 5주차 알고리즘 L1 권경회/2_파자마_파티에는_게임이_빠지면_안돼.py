from queue import Queue

n, k, m = [int(v) for v in input().split()]


def pajamas_game(n, k, m):

    q = Queue()
    result = []

    for i in range(1, n+1):
        q.put(i)

    while not q.empty():
        for i in range(k):
            num = q.get()

            if i == k-1:
                result.append(num)
            else:
                q.put(num)

    return result.index(int(m))+1


print(pajamas_game(n, k, m))

"""
40점 / 시간초과
"""
