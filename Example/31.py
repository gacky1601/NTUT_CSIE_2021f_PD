a=input().split()
aa=list(map(int,a))
sex={}
for i in aa:
    sex[i] =sex.get(i,0) +1#0是必須的,因為一開始甚麼都沒有,所以回傳0給他
answer=str(min(sex.keys()))#字典左邊叫KEY 右遍叫value ex:  1 :  4  加上str因為我們要用字串形式相加 代表answer[0]='1'
sex[int(answer)]=sex[int(answer)]-1#沒加int的話,會噴錯找不到KEY直
for j in range(1,len(aa)):#
    for k in sorted(sex.keys()):#排列過的數字
        if answer[j-1]!=str(k) and sex[k]!=0:
            answer+=str(k)
            sex[k]-=1
            break
small=answer[-1]#最後的字
last=len(answer)-1
while(sex[int(small)]!=0):
    if last==0:
        answer=small+answer
        break
    if answer[last]!=small and  answer[last-1]!=small:
        answer = answer[:last] + small +answer[last:]
        sex[int(small)]-=1
    last-=1
print(answer)