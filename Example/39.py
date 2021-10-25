def number(a):
    #a=int(a,2)#二轉10
  
    k=0
    for i in range (0,8):
        if a[i]=='1':
            k = k + 2**(7-i)
    return k
def number1(a):
    a=bin(a)
    a=str(a)
    word=a.replace('0b','00000')
    print(word[-4:])
    return a
def c(a):
     b=0
     if a == 0 or a == 1:
         
         return b  
        
     if   a%2==0:
         
        return c(a/2) +1
    
     if   a%2==1:     
        return c((a+1)/2)  +1
    
        
while  True:
    a=input()
     
    sex=number(a)
    sex1=c(sex)
    b=input()
    number1(sex1)
    if b=='-1':
        break
    
    
    
    
    
