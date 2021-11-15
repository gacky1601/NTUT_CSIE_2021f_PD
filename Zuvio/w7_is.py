def isPrime(n):
    a=True
    if n >1:
        for i in range (2,n):
            if (n%i == 0):
                a= False
                break
        else:
            a= True
    else:
        a= False
    return a

a=int(input())
b=[number for number in range (2,a) if isPrime(number)]
print(sum(b))