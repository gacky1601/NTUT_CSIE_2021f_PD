a=input()
b=int(input())
c=int(input())
x=float(c/((b/100)**2))

if (x<=18.5):
    print("Hi %s, Your BMI: %f too LOW."%(a,x))
elif (x>=24):
     print("Hi %s, Your BMI: %f too HIGH."%(a,x))
else :     
     print("Hi %s, Your BMI: %f."%(a,x))
     
     
     
