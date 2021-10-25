a=input()
b=input()
c=input().split()
d=input().split()
money=[0,0,0,200,1000,4000,10000,40000,200000]
total=0
def sex():
    if i1==a:
        return 10000000
    if i1==b:
        return 2000000
    for j in range(8,2,-1):
        for k in c:#這行需要
            if i1[-j:]==k[-j:]:#這裡是[-J:]
                return money[j]
    for o in d:
        if i1[-3:]==o:
            return 200
    return 0
for i in range(int(input())):
    i1=input()
    total+=sex()
print(total)
