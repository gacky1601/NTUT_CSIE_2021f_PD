# 迴圈偶數連加，輸入兩整數a、b，且a 例如輸入 a=1、b=100，則輸出結果為 2550(2+4+6+8+ ... +100 =2550)
# simple input:
# 1
# 100

# simple output:
# 2550

num1,num2=int(input()),int(input())
x=0
if num1%2 !=0:
    num1+=1
if num2%2 !=0:
    num2+=1

for i in range(num1,num2+2,2):
    x+=i

print (x)

