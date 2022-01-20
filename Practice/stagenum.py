a=int(input())
for i in range(a):
    b=str(i)
    u=True
    for j in range(len(b)-1):
        if b[j]>b[j+1]:
            u=False
            break
    if u:
        print(b)