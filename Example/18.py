'''*將每個功能的Code寫成2個function，每一個function使用一層迴圈*
*亦即一個 function 不要有兩個迴圈/巢狀迴圈*
請使用 while loop或for loop
第一個輸入意義為選擇三種圖形:
1 直角三角形
2 正三角形
3 倒三角形

第二個輸入意義為畫幾行
(輸出圖形為數字+底線)

input
1 (第一種圖形：直角三角形)
5 (共 5 行)
--------------------------
output
1
121
12321
1234321
123454321
---------------------------
input
2 (第二種圖形：正三角形)
4 (共 4 行)
---------------------------
output
___1___
__121__
_12321_
1234321
--------------------------
input
3 (第三種圖形：倒三角形 )
3 (共 3 行數)
---------------------------
output
12321
_121_
__1__'''

q='_'   
def x (n,mark):
    if mark=='_':
        for x3 in range(1,n+1,1):
            print("_",end="")
        
    else:   
        for x1 in range(1,n+1,1):
            print(x1,end='')
        for x2 in range(n-1,0,-1):
            print(x2,end='')
    
def o (a,b):
    if a=='1':
       for o1 in range (b+1,-1,-1):
           x(b-o1,o1)
           
           print('')
    elif a=='2':
        
         for o2 in range(b-1,-1,-1):
             x(o2,q)
             x(b-o2,o2)
             x(o2,q)     
             print('')
    elif a=='3':
         for o3 in range(0,b,1):
             x(o3,q)
             x(b-o3,o3)
             x(o3,q)
             print('')
a=input()
b=int(input())
o(a,b)
   
       
        
        


