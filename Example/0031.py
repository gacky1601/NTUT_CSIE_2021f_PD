a=input().split()
aa=list(map(int,a))
sex={}
for i in aa:
    sex[i]=sex.get(i,0)+1
answer=str(min(sex.keys()))
sex[int(answer)]=sex[int(answer)]-1
for j in range(1,len(aa)):
    for k in sorted(sex.keys()):
        if answer[j-1]!=str(k)  and sex[k]!=0:
            answer+=str(k)
            sex[k]-=1
            break
small=answer[-1]
last=len(answer)-1
while sex[int(small)]!=0:
    if last==0:
        answer=small+answer
        break
    if answer[last]!=small and answer[last-1]!=small:
        answer=answer[:last] +small+answer[last:]
        sex[int(small)]-=1
    last-=1
print(answer)