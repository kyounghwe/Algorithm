n,k = map(int,input().split())
sum_num =0
for i in range(0,n+1):
    sum_num += i ** k
print(sum_num%1000000009)
