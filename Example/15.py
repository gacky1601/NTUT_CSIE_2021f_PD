a=int(input())
b=[0]*a#不能打b=[],系統不接受
for x in range(0,a):
    b[x]=int(input())
b.sort()
print(b[a-2])   
print(b[0]*b[a-1]) 
    