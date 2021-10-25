A,B,x,y=input(),input(),input(),input()
C=A+B
D = C.replace(x,y)
print(len(C)+len(D))
E=D[0:3:]+D[-3:len(D):]
print(E*3)