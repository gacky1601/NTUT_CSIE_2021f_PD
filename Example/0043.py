sex={}
for i in range(int(input())):
    i1=input().split()
    sex[i1[0]]=i1[1:]#這裡要確定是
for k in range(int(input())):
    k1=input().split('+')
    for j in k1:
        j=j.split()
        for collname in sex:#sex沒有括號
            match=True
            for feature in j :
                if feature not in sex[collname]:#sex配合中括號
                    match=False
                    break
            if match:
                print(collname,end=' ')
    
        


    

