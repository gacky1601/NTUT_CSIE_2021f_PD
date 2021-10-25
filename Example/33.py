
def sex(x,y):
    while x> 0 and y>0 :
        if x>y:
            x=x%y
        else :
            y=y%x
    return(x if x>y else y)

while True:
    a=input().split()
    if a[0]=='-1':
        break
    else:
        array=list(map(int,a))
        b=sex(array[0],array[1])
        c=sex(b,array[2])
        print(c)
        
    
    