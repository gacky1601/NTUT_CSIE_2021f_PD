n=input()
a=[]
for i in range(int(n)):
    b=input().split(",")
    a.append([int(b[0]),int(b[1])])
a.sort(reverse=True)
# c=[]
# print(a)
# if a[0][1] >= a[1][0]:
#     c.append([a[0][0],a[1][1]])
# else:
#     c.append([a[0][0],a[0][1]])
#     c.append([a[1][0],a[1][1]])
# print(c)

if a[0][0]>=a[1][0] and a[0][1]<=a[1][1]:
    a.remove(a[0])
print(a)