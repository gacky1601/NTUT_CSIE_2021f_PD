
n=int(input())
sex=0
x=0
array=[[0]*2 for o in range(n)]
for o in range(n):
    n1=input().split(' ')
    array[o][0]=int(n1[0])
    array[o][1]=int(n1[1])
array.sort()
for o1 in range(n):
    p=int(array[o1][0])
    z=int(array[o1][1])
    if  sex>p:
        x+=max(z-sex,0)
    else :
        x+=max(z-p,0)
    if z>sex:
        sex=z
print(x)
    
