sex=[]
for i in range(int(input())):
    sex.append( input())
key=input().split()
sex1=[]
num=0#第幾筆資料
for j in sex:
    time=0
    for k in key:
        for l in range(len(j)-len(k)+1):
            if j[l:l+len(k)].upper()==k.upper():
                j=j[:l]+k.upper()+j[l+len(k):]
                time+=1
    num+=1
    sex1.append([time,-num,j])
for o in sorted(sex1,reverse=True):
    print(o[2])





