q='_'   
def x (n,mark):
    if mark=='_':
        for x3 in range(1,n+1,1):
            print("_",end="")
        
    else:   
        for x1 in range(1,n+1,1):
            print(x1,end='')
        for x2 in range(n-1,0,-1):
            print(x2,end='')
    
def o (a,b):
    if a=='1':
       for o1 in range (b+1,-1,-1):
           x(b-o1,o1)
           
           print('')
    elif a=='2':
        
         for o2 in range(b-1,-1,-1):
             x(o2,q)
             x(b-o2,o2)
             x(o2,q)     
             print('')
    elif a=='3':
         for o3 in range(0,b,1):
             x(o3,q)
             x(b-o3,o3)
             x(o3,q)
             print('')
a=input()
b=int(input())
o(a,b)
   
       
        
        


