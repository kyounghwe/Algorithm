s = input()
t = input()

s_string = ''
t_string = ''

result = 0

while len(s_string) < 50:
    s_string += s

while len(t_string) < 50:
    t_string += t

for i in range(0, 50):
    if(s_string[i] == t_string[i]):
        result = 1
        continue
    else:
        result = 0
        break

print(result)
