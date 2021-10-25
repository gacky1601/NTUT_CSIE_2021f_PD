a=input()
string=' '
for i in a:
    if i.isdigit():
        print(i,end='')
    elif i not in string:
        num=a.count(i)
        if num<10:
            print(num,end='')
        string+=i

