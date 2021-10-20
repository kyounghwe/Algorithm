T = int(input())

a = int(input())
a_n = list(map(int,input().split()))

c=int(input())
c_n = list(map(int,input().split()))

ali = []
che = []

# 방법1
def allcount(num,lists2):
    lists1=[]
    lists1.append(sum(lists2[0:num]))
    for i in range(num):
        lists1.append(lists2[i])
        for j in range(2,num):
            if i+j<=num:
                lists1.append(sum(lists2[i:i+j]))
    return lists1

    
ali = []
che = []
ali = allcount(a,a_n)
che = allcount(c,c_n)


# count =0
# for i in range(len(ali)):
#     for j in range(len(che)):
#         if ali[i]+che[j] == T:
#             count +=1
# print(count)

count =0
if a>c:
    for i in ali:
        if T-i in che:
            count+=1
else:
    for i in che:
        if T-i in ali:
            count+=1
print(count)
