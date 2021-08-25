def check(s, t):
    if len(s) > len(t) :
        for i in range(len(t)):
            if s[i] != t[i]:
                return 0
        return 1


    elif len(s) < len(t) :
        for i in range(len(s)):
            if s[i] != t[i]:
                return 0
        return 1
        
s = input()
t = input()

result = check(s, t)
print(result)
