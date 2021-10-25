a=input().split(' ')
array=[]
for a1 in range(len(a)):
    a[a1]=int(a[a1])
a.sort()
for a2 in range(len(a)):
    if a[a2]%2==1:
        array.append(a[a2])
a.reverse()
for a3 in a:
    if a3%2==0:
        array.append(a3)
print(array)

