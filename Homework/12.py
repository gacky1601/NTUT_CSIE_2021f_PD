# mr = [[0.08, 0.07, 0.06],[0.1393, 0.1304, 0.1087],[0.1349, 0.1217, 0.1018],[1.1287,1.1127,0.9572],[1.4803,1.2458,1.1243],[183, 383, 983]]
x=[0,0,0,0,0]
x[0],x[1],x[2],x[3],x[4]=int(input()),int(input()),int(input()),int(input()),int(input())
mr=[[0.08, 0.1393, 0.1349, 1.1287, 1.4803, 183], [0.07, 0.1304, 0.1217, 1.1127, 1.2458, 383], [0.06, 0.1087, 0.1018, 0.9572, 1.1243, 983]]
p=[0,0,0,0]

for i in range(0,3):
      for j in range(0,5):
            p[i]=p[i]+x[j]*mr[i][j]
            if(j==4):
                  
                  if((p[i]-mr[i][5])>0):
                        p[i]=p[i]
                  elif((p[i]-mr[i][5])<=0):
                        p[i]=mr[i][5]      
      p[i]=int(p[i])

if p[0]>p[1]:
    if p[1]>p[2]:
        print('Type 983')
    else:
        if p[0]>p[2]:
            print('Type 383')
        else:
            print('Type 383')
elif p[0]<p[1]:
    if p[1]<p[2]:
        print('Type 183')
    else:
        if p[2]>p[0]:
            print('Type 183')
        else:
            print('Type 983')

