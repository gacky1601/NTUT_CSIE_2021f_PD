'''004
輸入身高(公尺) 體重(公斤)(皆使用小數)

BMI = 體重(公斤) / (身高*身高)(公尺)

結果須輸出到小數點第一位
print("%.1f" %x1);

輸入:
1.72
60

輸出:
20.3
'''

height,weight=float(input()),float(input())
bmi= weight/(height*height)
print("%.1f" %bmi)