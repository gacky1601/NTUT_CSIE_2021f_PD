import math
a=int(input())
b=int(input())
c=int(input())
x1 =float(((-b)+math.sqrt(b*b-4*a*c))/(2*a))
x2 =float(((-b)-math.sqrt(b*b-4*a*c))/(2*a))
print("%.1f" % x1)
print("%.1f" % x2)
