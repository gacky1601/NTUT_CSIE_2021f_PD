def x (n,mark):
    for x1 in range(n,0,-1):
        print(x1,end='')
        
a=int(input())
b=1
c='#'
for p1 in range(a,a*2,1):
    print(c*p1,end='')
    x(a*2-p1,b)
    print('')
      
    

