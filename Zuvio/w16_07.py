import numpy as np
x=4
d= [[i]*x for i in range(x)]
a=np.array(d)
print(a[2])
for i in range(x):
    djdd=a[:,2]
    m=(a[:,1]==2)
    print (m.sum(),end='')
print('\n',np.sum(a,axis=0))
print(np.sum(a))

# a=np.linspace(0,11,12).reshape([3,4])
# print(a[1:2,2:3])
# print(np.sum(a,axis=0))
# print(np.sum(a,axis=1))
# print(np.sum(a))