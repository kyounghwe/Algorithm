side_list = []

for _ in range(3):
    sides = list(map(int, input().split()))
    if sides[0] == 0:
        break
    side_list.append(sides)

#print(side_list)

for side in side_list:
    Max_side = max(side)
    side.remove(Max_side)
    
    if (Max_side**2) == (side[0]**2) + (side[1]**2):
        print('rightangle')
    else:
        print('triangle')
