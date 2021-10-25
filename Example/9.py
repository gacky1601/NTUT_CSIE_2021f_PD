a=int(input())
b=int(input())
c=int(input())
if 0<=a<=10:
   ax=30*a
elif a<=15:
     ax=30*a*0.95
elif a<=20:
     ax=30*a*0.9
elif a>=21:
     ax=30*a*0.8
     
if 0<=b<=10:
     bx=70*b
elif b<=15:
     bx=70*b*0.9
elif b<=20:
     bx=70*b*0.85
elif b>=21:
     bx=70*b*0.75
     
if 0<=c<=10:
     cx=40*c
elif c<=15:
     cx=40*c*0.85
elif c<=20:
     cx=40*c*0.8
elif c>=21:
     cx=40*c*0.8
if a+b+c>=30:
   sum=ax+bx+cx
   sum=int(sum*0.87) 
print (sum )    
    
