hurry=[]
for i in range(0,4):
    hurry.append(int(input()))

x = sum(hurry)/60
y = sum(hurry)%60

print(int(x))

print(y)
