N = int(input())
H = list(map(int, input().split()))
cnt = 0

while len(H) > 0:
    max_high = max(H)
    i=0
    
    while max_high > 0:
        try:
            if H[i] == max_high:
                del H[i]
                max_high -= 1
            else:
                i += 1
        except IndexError:
            break
    
    cnt += 1

print(cnt)
