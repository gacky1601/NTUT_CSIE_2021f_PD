'''
階梯數字：數字字串從高位數往低位數看過去，每一位數字只會相等或變大，例如：9、234、777、11222233等數字都有這性質，稱階梯數字(0不是階梯數字)。

給定一正整數 N>0，找出不大於N的階梯數字共有幾個。

輸入說明： 一個正整數N。
輸出說明:：一個不大於N的階梯數字總個數。

Sample Input1：
25
Sample Output1：
22

Sample Input2：
23456
Sample Output2：
1365

Sample Input3：
54321
Sample Output3：
1875

Sample Input4：
88888888
Sample Output4：
24301

Sample Input5：
9999999999999999999999999999
Sample Output5：
124403619

註：執行時間過長會導致測試失敗
'''

n = input()
table = [[1]*(10) for i in range(len(n) + 1)]
print(table)
total = 0
maxNum = int(n[0])
isLadder = 1

for i in range(2, len(n) + 1):
    for j in range(8, 0, -1):
        table[i][j] = table[i][j + 1] + table[i - 1][j]
for i in range(1, len(n)):
    for j in range(1, 10):
        total += table[i][j]
    isLadder = isLadder if n[i - 1] <= n[i] else 0
for i in range(1, int(n[0])):
    total += table[len(n)][i]
for i in range(1, len(n)):
    while maxNum < int(n[i]) and n[i - 1] <= n[i]:
        total += table[len(n) - i][maxNum]
        maxNum += 1
total += 1 if isLadder else 0

print(total)