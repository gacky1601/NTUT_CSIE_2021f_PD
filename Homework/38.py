a=input()
b=[]
for i in range(len(a)+1):
    for j in range (len(a)+1):
        x=a[i:j]
        # if x not in a:
        if x==x[::-1]:
            if x!='':
                if x not in b:
                    b.append(x)
b.sort()
gg=""
for i in b:
    gg=gg+i+"#"

print(gg[:len(gg)-1])