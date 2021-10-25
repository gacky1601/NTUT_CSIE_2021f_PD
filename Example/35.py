def k (a):
    array=[]
    if len(a)==1:
        return a
    for i in range(len(a)):
        for j in k(a[:i]+a[i+1:]):
           sex=[] 
           sex.append(a[i])
           sex+=j
           array.append(sex)
           
           
    return array
a=input().split()
a.sort()
sex1=k(a)
for j in  range(len(sex1)):
    sex2=list(map(int,sex1[j]))
    print(sex2,end='')
    if j ==len(sex1)-1:
        print()
    else:
        print(',')
    
