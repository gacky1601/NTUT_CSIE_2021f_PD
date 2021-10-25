a=input().split(' ')
b0=int(a[0])
b1=int(a[1])
b2=int(a[2])
b3=int(a[3])
b4=int(a[4])
b5=int(a[5])
x=0
c=0
while True:
        x+=1
        if (x%b0==b1 and x%b2==b3 and x%b4==b5):
            print(x)
            break
        else:
            c+=1

    

