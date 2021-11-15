'''001
某一學生修國文Chinese、計算機概論CS、計算機程式設計PD三科，使用者輸入名字（一個string）、學號（int）、三科成績(int)。
(1) 計算學生總成績、平均。
(2) 印出名字、學號、總成績、平均。
(3) 輸出的數字如為整數，不需含有小數點。

Input:
Tom
905067
100
100
100

Output:
Name:Tom
ID:905067
Average:100
Total:300
'''
name = input()
sid = int(input())
chinese = int(input())
cs = int(input())
pd= int(input())
total=(chinese+cs+pd)
print("Name:"+name)
print("ID:"+str(sid))
print("Average:"+str(total//3))
print("Total:"+str(total))