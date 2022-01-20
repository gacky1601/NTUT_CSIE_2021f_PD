def addOne(n):
    u=1
    for i in range (len(n)-1,-1,-1):
        if int(n[i])<9:
            n=n[:i]+str(int(n[i])+u)+n[i+1:]
            u=0
        else:
            n=n[:i]+"0"+n[i+1:]
            u=1
    if u==1:
        n="1"+n
    return n


print(addOne("29999999999999999999999999999999999999999999999999999999"))