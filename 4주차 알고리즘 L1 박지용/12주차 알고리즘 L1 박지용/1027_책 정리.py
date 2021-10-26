N = int(input())
book_list = list(map(int, input().split()))
new_list=[]

#print(book_list)
#print(new_list)

new_list.append(book_list[0])

cnt = 0
for i in range(1, len(book_list)):
    if new_list[i-1] < book_list[i]:
        new_list.append(book_list[i])
    else:
        new_list.insert(i-1, book_list[i])
        cnt += 1

print(cnt)
