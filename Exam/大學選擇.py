def sch_in():
    times=int(input())
    temp={}
    for i in range (times):
        rule={'BC':0,'NC':0,'CT':0,'NS':0,'NM':0,'HL':0,'NL':0}
        temp_rule={}
        b=input().split(" ")
        temp_rule=rule
        for i in range(1,len(b)):
            if b[i] in temp_rule.keys():
                temp_rule[b[i]]=1
            # print(i,",",temp_rule)
            temp[b[0]]=temp_rule
    print(temp)
    return temp
x=sch_in()
def cond():
    x={}
    u=list(input().split(" + "))
    # print(u)
    for i in u:
        if i[0]=='!':
            x[i[1:]]=0
        else:
            x[i]=1
    # print(x)
    return x
y=cond()
l={}
for j in x.keys():
    for i in y.keys(): 
        if x[j][i]==y[i]:
            try:
                l[j]+=1
            except:
                l[j]=1
        else:
            continue

x=sorted(l.items(),key=lambda x:x[1],reverse=True)

pp=str()

for i in range(len(x)):
    pp+=x[i][0]+","+str(x[i][1])+" "
print(pp[:-1])
