# 請使用 while loop或for loop
# 第一個輸入意義為選擇三種圖形:
# 1 三角形方尖方面向右邊
# 2 三角形方尖方面向左邊
# 3 菱形

# 第二個輸入意義為畫幾行
# (奇數，範圍為 3,5,7,9,....,21)

# input
# 1 (第一種圖形，三角形尖方面向右邊)
# 9 (共 9 行)
# --------------------------
# output
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# ---------------------------
# input
# 2 (第二種圖形，三角形尖方面向左邊)
# 5 (共 5 行)
# ---------------------------
# output
# ..*
# .**
# ***
# .**
# ..*
# --------------------------
# input
# 3 (第三種圖形: 菱形 )
# 3 (共 3 行數)

# 輸出
# .*
# ***
# .*

def myprint(n,mark):
    for i in range(n):
        print(mark, end='')

def prymid(row):
    row=int((row/2))+1
    for i in range (1,row+1):
        for j in range (0,i):
            print("*",end='')
        print('')
    for x in range (i-1,0,-1):
        for y in range (x,0,-1):
            print("*",end='')
        print('')

def prymid_l(row):
    row=int((row/2))+1
    for i in range(1,row+1):
        myprint((row-i),'.')
        myprint(i,'*')
        print()
    for j in range(row-1,0,-1):
        myprint((row-j),'.')
        myprint(j,'*')
        print()

def rhombus(row):
    row+=2
    row2=int(row/2)-1

    for i in range(1,row,2):
        myprint(row2,'.')
        myprint(i,'*')
        print()
        row2-=1
    row2+=1
    for j in range(i-2,-1,-2):
        row2+=1
        myprint(row2,'.')
        myprint(j,'*')
        print()
        
shape=int(input())
row=int(input())

if(shape==1):
    prymid(row)
elif(shape==2):
    prymid_l(row)
elif(shape==3):
    rhombus(row)
else:
    pass
