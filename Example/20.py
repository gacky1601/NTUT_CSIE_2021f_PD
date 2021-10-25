a=int(input())
b=0
for a1 in range(2,a):
    if (a%a1==0):
        b=1
        break

if (b==0):
    print("%d is prime number" % a)
         
    
else:       
    print("{} is not prime number".format(a))
