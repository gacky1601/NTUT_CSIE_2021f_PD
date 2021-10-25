a=input()
b=input()
c=input().split()
d=input().split()
total=0
money=[0,0,0,200,1000,4000,10000,40000,200000]
def sex():
    if i1==a:
        return 10000000
    if i1==b:
        return 2000000
    for j in range(8,2,-1):
        for k in c:
            if i1[-j:]==k[-j:]:
                return money[j]
    for z in d:
        if i1[-3:]==z:
            return 200
    return 0
for i in range(int(input())):
    i1=input()
    total+=sex()
print(total)


    
                
            

        
           
        


