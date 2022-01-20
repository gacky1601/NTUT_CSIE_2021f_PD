'''39.
輸入說明：
輸入一個大小寫英文字串和一個數字n，以一個空格間隔，且n需小於等於字串的長度，字串中不得有空格且字元不得重複，字串長度不得超過8字元

輸出說明：
計算出對字串取n個字元的所有組合可能，組合內依原字串中字元順序排序，再對所有組合可能依字典順序排序後，依序以一個空格間隔輸出。
==============
Sample input 1:
ABCD 2

Sample output 1:
AB AC AD BC BD CD
==============
Sample input 2:
pekoPEKO 8

Sample output 2:
pekoPEKO
==============
Sample input 3:
pelican 3

Sample output 3:
can ean eca ecn eia eic ein ela elc eli eln ian ica icn lan lca lcn lia lic lin pan pca pcn pea pec pei pel pen pia pic pin pla plc pli pln
==============
Sample input 4:
Guavb 4

Sample output 4:
Gavb Guab Guav Guvb uavb
==============
Sample input 5:
DinoSaur 5

Sample output 5:
DSaur DiSar DiSau DiSur Diaur DinSa DinSr DinSu Dinar Dinau DinoS Dinoa Dinor Dinou Dinur DioSa DioSr DioSu Dioar Dioau Diour DnSar DnSau DnSur Dnaur DnoSa DnoSr DnoSu Dnoar Dnoau Dnour DoSar DoSau DoSur Doaur iSaur inSar inSau inSur inaur inoSa inoSr inoSu inoar inoau inour ioSar ioSau ioSur ioaur nSaur noSar noSau noSur noaur oSaur'''


# a=input().split(" ")
# b=a[0]
# cond=int(a[1])
# c=[]
# for i in range (len(b)):
#     for j in range(i+1,len(b)):
#         s=b[i]
#         for k in range(0,cond-1):   
#             if j+k <len(b):
#                 s+=b[j+k]
#         if(len(s)==cond):
#             c.append(s)
#         s=""
# c.sort()
# print(c)

def find(str,num):
    if num==1:
        return [ch for ch in str]
    x=[]
    for i in range(len(str)):
        for j in find(str[i+1:],num-1):
            # print(j)
            x.append(str[i]+j)
    return x
a=input().split(' ')
b=find(a[0],int(a[1]))
b.sort()
s=''
for i in b:
    s+=i+" "
print(s[:len(s)-1])
