def num(x):
    
    if (x=='J' or x=='K' or x=='Q'):
        x=0.5
        return (x)
    elif (x=='A'):     
        x=1
        return (x)
    else :
          return int(x) 
a1=input().split(' ')     
a=num(a1[0])
b=num(a1[1])
count1=0
count2=0


while True:
    a1=input().split(' ')
    c=num(a1[0])
    print(c,type(c)) 
    if c ==0:
        d=num(a1[1])
        if d==1:
            c1=num(a1[2])
            b+=c1
            count2+=1
        elif d==0:
            break
    if c == 1:
        d=num(a1[1])
        a+=d
        count1+=1
        c1=num(a1[2])
        if c1==1:
            d1=num(a1[3])
            b+=d1
            count2+=1
            

    if (a>21) :
        a=0
        break
    if (b>21):
        b=0
        break
        
   
    if(count1==4 or count2==4):
        break
    
if(a>b and a<=21):              
    print("Player X is Winner")    
elif(b>a  and b<=21):
    print("Player Y is Winner")
    
    
    
if(a==0):
     print("Player X $ Bang!")
elif(a<=21 and a%int(a)!=0):
    print("Player X $ %.1f" % a)
elif(a<=21):
    print("Player X $ %d" % a)
    
if(b==0):
     print("Player Y $ Bang!")
elif(b<=21 and b%int(b)!=0):
    print("Player Y $ %.1f" % b)
elif(b<=21):
    print("Player Y $ %d" % b)
    