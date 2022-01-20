'''40.
(1)首先，輸入一串不超過50字元的字串(不得有空格)及一正整數K，兩者以一個空格為間隔
(2)去除字串間非英文字母的字元，例如the$sky@iS!soBlue 應轉換成theskyiSsoBlue
(3)再對字串做大小寫的互相轉換，例如theskyiSsoBlue 應轉換成 THESKYIsSObLUE
(4)對字串以每隔K個字元進行切割，最後一組若字元數不足K則無視
例如：當K=3時，THESKYIsSObLUE 應切割成THE、SKY、IsS、ObL、UE共計5組字串
(5)將每組切割好的字串進行順序反轉後，並以【/】作為間隔輸出。
例如：THE、SKY、IsS、ObL、UE應轉換並輸出UE/ObL/IsS/SKY/THE
==============
Sample input 1:
abcda 1

Sample output 1:
A/D/C/B/A
==============
Sample input 2:
abcDefgHiaaA 2

Sample output 2:
Aa/IA/Gh/EF/Cd/AB
==============
Sample input 3:
mynameisBig5666hehe 10

Sample output 3:
GHEHE/MYNAMEISbI
==============
Sample input 4:
iHaveAnApple 15

Sample output 4:
IhAVEaNaPPLE
==============
Sample input 5:
@H#hHhhhh12*4%H287 3

Sample output 5:
Hh/HHH/hHh'''
d=[]
def numcheck(str):
    if str.isupper() or str.islower():
        return str.swapcase()
    else:
        return ""

def myprint(str,num):
    global d
    if len(str)<num:
        d.append(str)
    else:
        d.append(str[:num])
        # print(str[:num]+"/",end='')
        return myprint(str[num:],num)
x=input().split(" ")
a=x[0]
g=""
for i in a:
    g+=numcheck(i)


myprint(g,int(x[1]))
s=''

if d[len(d)-1]=='':
    d.pop()
for i in range(len(d)-1,-1,-1):
    s+=d[i]+"/"
print(s[:len(s)-1])
