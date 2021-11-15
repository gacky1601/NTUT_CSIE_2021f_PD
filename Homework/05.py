'''005.
輸入一篇英文文章 ，文章中單字與單字之間以一個空白間隔。另外輸入兩個單字(word) P、Q。
P為文章中所出現的單字，Q為取代或加入的單字
(1) 在文章中把 P 字串以 Q 字串取代，並輸出。
(2) 在文章中把P 字串刪除，並輸出。

輸入範例說明:
第一行，文章
第二行，英文字 P
第三行，英文字 Q

輸出範例說明:
第一行，將文章中的 P 取代成 Q。
第二行，將文章中P單字刪除後印出


Sample Input

This is a book That is a cook
is
was

Sample Output

This was a book That was a cook
This a book That a cook
'''
sen,P,Q=input(),input(),input()
sen_sp=sen.split(' ')
temp=""
temp2=""
temp3=""
for i in range(0,len(sen_sp)):
    if((i+1)>=len(sen_sp)):
        if (sen_sp[i]==P):
            temp=temp+Q
            temp2=temp2+Q+" "+str(sen_sp[i])
        else:
            temp=temp+str(sen_sp[i])
            temp2=temp2+str(sen_sp[i])
            temp3=temp3+str(sen_sp[i])
    else:
        if (sen_sp[i]==P):
            temp=temp+Q+" "
            temp2=temp2+Q+" "+str(sen_sp[i])+" "
        else:
            temp=temp+str(sen_sp[i])+" "
            temp2=temp2+str(sen_sp[i])+" "
            temp3=temp3+str(sen_sp[i])+" "
print(temp)
print(temp2)
print(temp3)