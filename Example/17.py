a=input()
b=int(input())
t1=(b+1)//2
def m (n,mark):
    for m1 in range(n):
        print(mark,end='') 
        
if a=='1':
    for x in range(t1):
        for x1 in range(x):
            print('*',end='')
        print('')#行數的換行
        
    for f in range(t1,0,-1):
        for f1 in range(f):
            print('*',end='')
        print('')#行數的換行
        
if a=='2':
    for p in range(t1-1,-1,-1):
        m(p,'.')
        m(t1-p,'*')
        
        print('')   
    for p1 in range(1,t1,1):
        m(p1,'.')
        m(t1-p1,'*')
        print('')  
        
if a=='3':
    for g in range(t1-1,-1,-1):
        m(g,'.')
        m(t1-g,'*')
        m(t1-g-1,'*')
        print('')   
        
    for g1 in range(1,t1,1):
        m(g1,'.')
        m(t1-g1,'*')
        m(t1-g1-1,'*')
        print('')  
    
    
       
        
    
            
            
           
        
    

