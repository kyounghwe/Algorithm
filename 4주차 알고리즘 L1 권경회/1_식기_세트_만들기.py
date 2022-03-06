import math

c, s, e = map(int, input().split())

# 젓가락(1/2)의 갯수가 숟가락 갯수 보다 작거나 같은 때
if int(c/2) <= s:
    if s - int(c/2) >= e:
        print(int(c/2))

    else:
        e = e-(s-int(c/2))
        print(int(c/2)-math.ceil(e/3))


# 젓가락(1/2)의 갯수가 숟가락의 갯수 보다 클때
else:
    if int(c/2) - s >= e:
        print(s)

    else:
        e = e - (c - (s*2))
        print(s - math.ceil(e/3))
