s = str(input())
t = str(input())

count = 0
end = len(t)//len(s)
for i in range(0, end):
    if t[len(s)*i:len(s)+(i)*len(s)] == s:
        count +=1

if (s*count == t) or s[:len(t)] == t:
    print(1)
else:
    print(0)
