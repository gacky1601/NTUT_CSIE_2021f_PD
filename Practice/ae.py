def f01 (n):
    if (n > 10):
        return n
    else:
        return  ((n-1) + f01(2*n-2)) 


print(f01(3))
print(f01(4))
print(f01(5))
print(f01(6))