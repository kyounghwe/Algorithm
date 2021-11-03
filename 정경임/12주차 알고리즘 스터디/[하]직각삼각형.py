triangles = []

# 삼각형의 세 변의 길이 입력
for i in range(3):
    t = [int(t) for t in input().split()]  # == list(map(int, input().split()))
    
    if t[0] == 0:
        break
    
    triangles.append(sorted(t))


# 직각삼각형 구분
for tri in triangles:
    if tri[-1]**2 == tri[0]**2 + tri[1]**2:
        print("rightangle")
    else:
        print("triangle")
