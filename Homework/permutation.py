def f(s):
    if len(s)==1:
        return [s]
    result = []
    for i in range(len(s)):
        result += [s[i]+ sub for sub in f(s[:i]+s[i+1:])]
    return result
print(f('ABC'))
print(f('ABCD'))