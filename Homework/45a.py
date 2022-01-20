def add(x,y,s):
    if not x in s.keys():
        s[x]=[]
    s[x].append(y)
    return s
def findpath(data, current, path, target):
    while (len(current)!=0):
        temp=current.pop(0)
        newpath=path.pop(0)+[temp]
        if temp==target:
            return newpath
        for i in data[temp]:
            if i not in newpath and i not in current:
                current.append(i)
                path.append(newpath)
    return []
                
N,X,Y,Z=input().split()
N=int(N)
s={}
for i in range(N):
    x,y=input().split()
    add(x,y,s)
    add(y,x,s)
print(s)
path_1=findpath(s,[X],[[]],Y)
path_2=findpath(s,[Y],[[]],Z)
if not path_1 or not path_2:
    print("No way!")
else:
    print(len(path_1+path_2[1::]))
    print("-".join(path_1+path_2[1::]))