# def m(x):
#     return x*x
# def adder(x,y,z):
#     return x+y+z
# x1=[1,3,5,7]
# for x in map(m,x1):
#     print(x)
# print()
# print([m(x) for x in x1])
# x2=[2,4,6,8]
# x3=[100,100,100]
# print([adder(x,y,z) for x,y,z in zip(x1,x2,x3)])
# import functools as ft
# x=[4,3,1,2,5]
# a=ft.reduce(lambda s,e:s+e,x,0)
# print(a)
# a=ft.reduce(lambda x,y:x*y,x,0.5)
# print(a)

import math
# x=5
# r=range(1,x)
# a=list(filter(lambda x:x%2==1,r))
# print(a)
# a=list(filter(lambda x:math.sqrt(x)%1==0,r))
# print(a)

a=[1,2,3]
b=[4,5,6]
c=[7,8,9,10]
zipped=zip(a,b)
print(zipped)
print([x for x in zipped])
print([x for x in zip(a,c)])
