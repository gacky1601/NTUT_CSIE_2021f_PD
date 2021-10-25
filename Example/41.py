def sex (a):
    total=0
    if int(a[0])== 0:
        return 0
    if 0<int(a[0])<10: 
        if len(a)==1:
            total+=1
        else:
            total+=sex(a[1:])
    if 0<int(a[:2])<27:
        if len(a)==2:
            total+=1
        elif len(a)!=1:
            total+=sex(a[2:])
    return total 
a=input()
print(sex(a))