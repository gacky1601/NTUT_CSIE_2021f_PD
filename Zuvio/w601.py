def myPrint(n, mark):
    for i in range(n):
        print(mark, end='')


def myPrintT(N):
    for i in range(N):
        myPrint(i,'.')
        myPrint((N-i),"*")
        print()

myPrintT(4)