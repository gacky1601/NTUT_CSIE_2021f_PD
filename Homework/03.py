'''003
分別輸入 num1 num2 求出兩數的 Sum,Difference,Product,Quotient。

結果須輸出到小數點第二位
print("%.2f" %x1);

輸入:
25
2

NOTE:Difference為相差，並非25-2，而是兩數之間的差

輸出:
Difference:23.00
Sum:27.00
Quotient:12.50
Product:50.00

'''

a,b= float(input()),float(input())

print("Difference:%.2f" %abs(a-b))
print("Sum:%.2f" %(a+b))
print("Quotient:%.2f" %(a/b))
print("Product:%.2f" %(a*b))