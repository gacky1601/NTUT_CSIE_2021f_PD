a = input()
x=0
y=0
z=""
for i in a:
    if i.isupper():#抓的是I才會讓他運作
        x+=1#遇到大寫X就加一
    elif i.islower():
        y+=1
        z=z+i
if y==0:
   print("No lowercase letters",end='')
print(z)
print(len(a))
print(x)