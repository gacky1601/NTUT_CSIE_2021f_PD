
a=input().split(' ')
global number
number=[]
global flower
flower=[]
global k
k={}
global k1
k1={}
for i in range(2,15):
    k[i] = 0
    k1[i] = 0
def number1():     
    for i in range(5):
        number.append(int((a[i])[:-1]))
    return number
        
def flower1():
    for i in range(5):        
        flower.append(a[i][-1])
    return flower
number = number1()
flower = flower1()        
for sex2 in range(len(flower)):
    c=flower.count(flower[sex2])
    k1[(sex2)]=c   
for sex3 in range(len(number)):
    b=number.count(number[sex3])    
    k[number[sex3]]=b
def se1():
    pair=0
    for sex1 in range(2,15):
        if k[sex1]==2:
            pair+=1
            if pair==1:
                return 1

def se2 ():#兩張重複的牌
    pair=0
    for sex3 in range(2,15,1):
        if k[sex3]==2:
            pair+=1
            if pair==2:       
                return 1       
def se3 ():
    pair=0
    for sex3 in range(2,15):
        if k[sex3]==3:
            pair+=1
            if pair==3:
                return 1
def se4():
    count=0
    for sex4 in range(0,4):
        if (number[sex4]==number[sex4+1]-1):
            
           count+=1
        if (number1()==['13','14','2','3','4'] or number1()==['12','13','14','2','3']  or number1()==['11','12','13','14','2']or number1()==['14','2','3','4','5']): 
            count+=1
            if count ==1:
                return 1
def se5():
    
    for sex5 in range (len(flower)):
        if k1[sex5]==5:
           return 1
def se6():
    pair=0
    threehouse=0
    for sex3 in range(2,15):
        if k[sex3]==2:
            pair+=1
        if k[sex3]==3:
            threehouse+=1
        if (pair==1 and threehouse==1):
            return 1
def se7():
    
    for sex7 in range(2,15):
        if k[sex7]==4:
            return 1
    return 2
def se8():
    if (se4()==1 and se5()==1):
        return 1
if se8()==1:   
    print('8')
if se7()==1:
    print('7')
elif se6()==1:
    print('6')
elif se5()==1:
    print('5')
elif se4()==1:
    print('4')
elif se3()==1:
    print('3')
elif se2()==1:
    print('2')
elif se1()==1:
    print('1')
else:
    print('0')