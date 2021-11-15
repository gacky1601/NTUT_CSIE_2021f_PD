# 025
# 輸入一組五張的撲克牌，判斷並輸出牌型
# ===================
# 撲克牌花色及點數：

# 1. 四種花色黑桃、紅心、磚塊、梅花，分別定義為 S, H, D, C。
# 2. 花色大小：黑桃>紅心>方塊>梅花。
# 3. 牌面符號A, 2, ..,, J, Q, K，點數2~10為2~10, A為14，J 為11， Q 為12，K為13，共有52張牌。
# ===================
# 牌型種類：

# 散牌 : 一組撲克牌中沒有任何其餘花色牌型，編號0。
# 一對 : 兩張數字一樣為 Pair，編號 1。
# 兩對 : 2 組 Pair 的牌為 Two pair，編號 2。
# 三條 : 三張一樣數字的為 Three of a Kind，編號 3。
# 順子 : 數字連續的 5 張牌為 Straight，包括[2, 3, 4, 5, 6],.., [11, 12, 13, 14, 2], [12, 13 ,14, 2, 3], [13 ,14, 2, 3, 4], [14, 2, 3, 4, 5]，編號 4。
# 同花 : 五張同一花色的牌為 Flush，編號 5。
# 葫蘆 : Three of a Kind 加一個 Pair為 Full House，編號 6。
# 四條 : 四張一樣數字為 Four of a Kind，編號 7。
# 同花順 : 數字連續的 5 張且花色一樣為 Straight Flush，編號 8。
# ===================
# 輸入說明：
# 五張撲克牌，每張牌之間以空格區隔，且無排序順序，
# 撲克牌的輸入編碼規則為牌面符號+花色，例如 10S 表黑桃 10、7D 表磚塊 7，QC 表梅花 Q

# 輸出說明：
# 判斷輸入撲克牌的牌型，並輸出符合的牌型種類中編號最大的值。
# ===================
# Sample input 1：
# AH 2H 3H 4H 5H

# Sample output 1：
# 8
# ===================
# Sample input 2：
# QC KC 8S 7C AC

# Sample output 2：
# 0
# ===================
# Sample input 3：
# 10D AD KD QD 8D

# Sample output 3：
# 5
# ===================
# Sample input 4：
# KC 4S 9H 4H 4C

# Sample output 4：
# 3


def cardnum(cardnum):
    if cardnum[0]=='J':
        return 11
    elif cardnum[0]=='Q':
        return 12
    elif cardnum[0]=='K':
        return 13
    elif cardnum[0]=='A':
        return 1
    elif cardnum[0]=='1':
        return 10
    else:
        return int(cardnum[0])

def continuous(cardcollect):
    x=1
    for i in range (0,len(cardcollect)-1):
        if(cardnum(cardcollect[i])==cardnum(cardcollect[i+1])-1):
            x+=1
        else:
            continue
    return x

def same(cardcollect,type):
    x={}
    card=""

    for card in cardcollect:
        if card[0:2]=='10':
            if type ==0:
                try:
                    x[card[0:1]]+=1
                except:
                    x[card[0:1]]=1
            else:
                try:
                    x[card[2]]+=1
                except:
                    x[card[2]]=1
        else:
            try:
                
                x[card[type]]+=1
            except:
                x[card[type]]=1
    return x

card=input()
cardcollect=card.split(" ")

cardcollect.sort(key = lambda s: cardnum(s[0:2]))
# print(cardcollect)

a=same(cardcollect,0)
b=continuous(cardcollect)
c=same(cardcollect,1)
# print("a",a)
# print("b",b)
# print("c",c)
# print(list(c.values()))
if(a[max(a,key=a.get)]==5):
    print("8")
elif(a[max(a,key=a.get)]==3):
    if 2 in a.values():
        print(6)
    else:
        print(3)
elif (a[max(a,key=a.get)]==4):
    print(4)
elif (b==5):
    if(5 in c.values()):
        print(8)
    else:
        print(4)
elif (5 in list(c.values())):
    print(5)
elif (a[max(a,key=a.get)]==2):
    gg=list(a.values()).count(2)
    if(gg==1):
        print(1)
    elif(gg==2):
        print(2)
else:
    print(0)