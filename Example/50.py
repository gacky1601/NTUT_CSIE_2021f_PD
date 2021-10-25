lista=[]
listb=[]
listc=[]
if input() =='A':
    while True:
        da=input().split()
        if da!=['B']:
            lista.append(list(map(int,da)))
        else:
            break
    lista=[list(j) for j in zip(*lista)]
    while True:
        da=input().split()
        if da!=['0']:
            listb.append(list(map(int,da)))
        else:
            break
for aa in lista:
    te=[]
    for bb in listb:
        te.append(sum(list(map(lambda t : t[0]*t[1],zip(aa,bb)))))
    listc.append(te)
for k in listc:
    for o in k:
        print(chr(o),end='')
print()
