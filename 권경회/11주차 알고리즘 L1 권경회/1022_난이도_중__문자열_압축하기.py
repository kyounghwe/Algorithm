s = input()


def decom(x):

    x = x.replace(")", "")
    b = x.find('(')

    if b == -1:
        return len(x)
    else:
        for i in range(len(x)-1, -1, -1):
            if x[i] == "(":
                n = int(x[i-1]) * x[i+1:]
                x = x[:i-1] + n
                return decom(x)


print(decom(s))
