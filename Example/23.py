def num(    ):
    x=input()
    if (x=='J' or x=='K' or x=='Q'):
        return 0.5
    elif (x=='A'):        
          return 1
    else :
          return int(x)   
a=num()
b=num()
c=1   #玩家選擇能不能抽排
d=1  #電腦選擇能不能抽排

while c==1:#T要大寫
    a1=input()
    if (a1=='Y'):
        a+=num()
    elif (a1=='N'):
        c=0
    while (d):#電腦要抽排符合的條件,能不能
        if (b<a or b<=8):   #需不需要     
            b+=num()
        else:
            d=0
        if c==1:#這樣才會回到18行去做判斷
            break
    if a>10.5:
        a=0
        c=0
    if b>10.5:
        b=0
        d=0
   
print('%.1f vs. %.1f' %(a,b))
if a>b:
    print("player wins")
elif b>a:
    print('computer wins')
else:
    print("It's a tie")
    
        
        
                 
    
 

    