dex={}
for i in range(int(input())):
    i1=input().split()
    dex[i1[0]]=i1[1:]
for j in range(int(input())):
    j1=input().split('+')
    for k in j1:
        k=k.split()
        for collname in dex:#這裡是把大學名稱抓出來
            match=True
            for feature in k:
                if feature not in dex[collname]:#有沒有對應的特色
                    match=False
                    break
            if match:
                print(collname,end=' ')
    print()
    