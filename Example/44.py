a1=int(input())
print('menu = {')
for j in range(a1):
    a=input().split()
    print("  '%s': {" % a[0])
    print("    'hours': '%s-%s'," %(a[1],a[2]))
    print("    'items': {")
    sex=''
    num=a[3:]
    for k in range (len(num)):
        if num[k].isdigit(): #如果這個字串裡面只有數字,那他就是TRUE,K就是數字
            print("      '%s': '$%s'"% (sex[:-1],num[k]),end='')#-1是要解決那個空白
            sex=''
            if k!=len(num)-1:
                print(',')
            else:
                print()
        else:#現在這裡的K是字串
            sex+=num[k]+' '
    print("    }\n  }",end='')
    if j==a1-1:
        print()
    else:
        print(',')
print('}')  





