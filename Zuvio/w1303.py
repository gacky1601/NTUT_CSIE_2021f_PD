def check(x, y):
    x = str(x)
    y = str(y)
    xLen = len(x)
    for i in range(xLen-1):
        if x[i]==x[i+1]:
            return 0
    for i in range(10):
        if x.count(str(i))!=y.count(str(i)):
            return 0
    return 1
def f(n, m):
    for i in range(n, m+1):
        if check(i, m)==1:
            print(i)
            break
#f(1122,2211)
f(11112233,33221111)