# 階乘計算，例如5的階乘計為5!，其值為120，最大不超過15!。
# 例如 5!=5*4*3*2*1

# simple input:
# 5

# simple output:
# 120
x=1
num=int(input())
for i in range(1,num):
    x=x+(x*i)

print(x)