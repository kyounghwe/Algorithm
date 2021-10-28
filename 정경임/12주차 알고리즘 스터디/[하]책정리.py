n = int(input())  # 책의 개수
books = [int(i) for i in input().split()]  # 책 배열 순서

# 2차원 dp 생성 : 
dp  = [[0]*n for i in range(n)]

# 가장 긴 증가하는 수열 길이 계산
for i in range(n):
    dp[i][i] = 1
    for j in range(i+1, n):
        for k in range(j):
            if books[k] < books[j]:
                dp[i][j] = max(dp[i][j], dp[i][k]+1)

# 전체 길이에서 가장 긴 증가하는 부분 수열 제거 = 옮겨야 하는 최솟값
lis = 0
for i in range(n):
    lis = max(lis, max(dp[i]))

result = n - lis

print(result)
        
'''
< dp 문제 >
1. 가장 긴 증가하는 수열 구한다.
2. 전체 수열에서 가장 긴 증가하는 수열의 길이를 뺀다. = 움직여야 하는 개수 구할 수 있음
'''
    
'''sorted_books = sorted(books)
# books.sort() : 기존 리스트에 영향ㅇㅇ
# sorted(books) : 기존 리스트에 영향ㄴㄴ'''

# https://jjangsungwon.tistory.com/47 참고한 블로그
