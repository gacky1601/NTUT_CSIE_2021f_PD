def num(x):
    if (x=='J' or x=='K' or x=='Q'):
        x=0.5
        return int(x)
    elif (x=='A'):
          x=1
          return int(x)
    else :
          return int(x)   
a=num(input())
b=num(input())
c=num(input())
d=num(input())
e=num(input())  
f=num(input())   
ax=int(a+b+c)
bx=int(d+e+f)
         
if ax>10.5:
   ax=0
if bx>10.5:
     bx=0
print(ax)
print(bx)

if ax>bx:
   
   print("A Win")
elif ax<bx:
     
     print("B Win")
elif ax==bx:
     
     print("Tie")


