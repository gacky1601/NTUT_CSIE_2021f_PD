def f(data):
    n = len(data)
    if n<=1:
        return data
    for i in range(n):
        x=data[i]
        y=data[0:i]+data[i+1:n]
        r = x + f(y)
        print(r)
        return r


def f(s):
    if len(s)==1:
        return [s]
    result = []
    for i in range(len(s)):
        result += [s[i]+ sub for sub in f(s[:i]+s[i+1:])]
    return result
#print(f('ABC'))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
print(fibonacci(5))