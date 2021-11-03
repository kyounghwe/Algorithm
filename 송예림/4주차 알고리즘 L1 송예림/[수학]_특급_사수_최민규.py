n =int(input())
count=0

anw = []
count_list = []
sum_i =0
for i in range(1,400):
    sum_i += i 
    anw.append(sum_i)
for i in range(0, len(anw)):
    count = 0
    for j in range(1,anw[i]+1):
        if anw[i] % j == 0:
            count+=1
    if count >= n+1:
        print(anw[i])
        break

#80점 나왔습니다
