import itertools

n, m = map(int, input().split())

choices = itertools.product([i for i in range(1, n+1)], repeat=m)

for c in choices:
    # perm = []
    for i in range(m):  # m == len(p)
        print(c[i], end=' ')
    print()
    


'''
중복 순열 : 중복 가능한 n개 중에 r개를 나열하는 경우의 수(순서 O)로 product 함수에 repeat인자를 통해 이용할 수 있다.
ex)
import itertools
result = list(itertools.product((["1","2","3","4"]), repeat=2))

=> 경우의 수 16가지 출력
**경우의 수 : 16개
[('1', '1'),
 ('1', '2'),
 ('1', '3'),
 ('1', '4'),
 ('2', '1'),
 ...
 ('4', '4')]
'''

