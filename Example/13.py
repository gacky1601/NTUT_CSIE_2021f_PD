a=int(input())
b=int(input())
x=0
y=1
for i in range(a,b+1,2):#不是(a,b+2,2)才會正確
    x=x+i
print(x)
for i in range(a,b+1,3):
    y=y*i
print(y)
