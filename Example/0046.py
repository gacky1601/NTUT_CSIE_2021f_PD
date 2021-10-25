sex=[]
for i in range(int(input())):
    sex.append(input())#裡面釋放INPUT
key=input().split()
sex1=[]
count=0
for j in sex:
    time=0
    for k in key:
        for r in range(len(j)-len(k)+1):#這行是最後跑到的地方
            if j[r:r+len(k)].upper()==k.upper():
                j=j[:r]+k.upper()+j[len(k)+r:]#這裡要季的:
                time+=1    
    count+=1
    sex1.append([time,-count,j])
for o in sorted(sex1,reverse=True):
    print(o[2])


