def f(z):
    if (len(z)<=1):
        if z in [str(i) for i in range(10)]:
            return 1
        else:
            return 0
    if z[0] in [str(i) for i in range(10)]:
        return 1+f(z[1:])
    return f(z[1:])
def main():
    print(f('1_9f8276xe5432r!1^'))
    print(f('9'))
main()