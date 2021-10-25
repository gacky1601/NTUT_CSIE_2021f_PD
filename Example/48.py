a=input()
string=''
num=0
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[j] not in string:
            string+=a[j]
        else:
            if len(string)>num:
                num=len(string)
            string=''
            break
print(num)

