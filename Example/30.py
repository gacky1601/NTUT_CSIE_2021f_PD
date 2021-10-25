a=input().split()
b=input().split()
array={}
array1=list(map(int,b))#把b的值抓出來,map
array1.sort()
for x1 in range (0,len(a)): #只是把值變成int,
    array[int(b[x1])]=(a[x1])
for x2 in range(0,len(a)):
    print (array[array1[x2]],end='')
    #不是print(array[x2],因為array沒辦法指定對應fOR從x2開始的值
    #因此要用array1[]

