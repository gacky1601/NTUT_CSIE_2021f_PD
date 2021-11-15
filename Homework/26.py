""" 026 
設計十點半的遊戲賭盤 
=================== 
撲克牌點數 

牌面A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K 
A~10 點數分別為 1~10點，J, K, Q 皆為 0.5點。 

牌面總點數大於10.5點，即為爆牌且該方不得再要牌。 
=================== 
強制停止閒家要牌階段的條件 

1. 閒家爆牌，閒家立賠且閒家不得再要牌。 
2. 閒家總牌面為一張10搭配一張J、Q或K，莊家立賠且閒家不得再要牌。 
3. 閒家總牌面擁有五張牌且未爆牌，莊家立賠且閒家不得再要牌。 
=================== 
遊戲流程 (下列範圍皆包含上限及下限)： 
1. 輸入閒家人數，人數介於1~3人。 
2. 輸入各閒家下注點數，點數介於1~10點，每個點數之間用一個空格區隔。 
3. 閒家各派發一張牌，每張牌之間以一個空格區隔。 
4. 輪流進入各閒家要牌階段，輸入Y表示要牌，輸入N表示停牌，接著輸入點數，可持續要牌，直到該位閒家停牌或符合前述強制停止要牌階段的條件後，才會進入下一位閒家的要牌階段。 
5. 各閒家皆停牌後，莊家先發一張牌給自己，之後可選擇是否要牌，直到停牌或爆牌。 
6. 若莊家爆牌，則須賠點給未爆牌的閒家且遊戲結束。 
7. 莊家停牌後遊戲結束，將與未爆牌閒家分別比較點數，點數較大者勝，若點數相同則視為莊家勝。 
8. 輸出莊家與各閒家的賠點或勝點，賠點以負號表示，勝點以正號表示。 
=================== 
輸入範例註解： 
3 閒家人數為3人 
2 10 5 各閒家下注點數 
Q 3 10 各閒家獲派的第一張牌 
Y 第一位閒家選擇要牌 
2 第一位閒家獲得2 
Y 第一位閒家選擇要牌 
7 第一位閒家獲得7 
N 第一位閒家選擇停牌 
Y 第二位閒家選擇要牌 
8 第二位閒家獲得8，總點數11導致爆牌，閒家立賠且閒家不得再要牌 
Y 第三位閒家選擇要牌 
Q 第三位閒家獲得Q，總牌面為10和Q，莊家立賠且閒家不得再要牌 
8 莊家獲得第一張牌 
Y 莊家選擇要牌 
2 莊家獲得2 
N 莊家停牌 

輸出範例註解： 
Player1 -2 
Player2 -10 
Player3 +5 
Bank +7 
=================== 
Sample input 1： 
2 
7 4 
9 10 
Y 
A 
Y 
K 
N 
Y 
J 
6 
Y 
4 
Y 
K 
N 

Sample output 1： 
Player1 -7 
Player2 +4 
Bank +3 
=================== 
Sample input 2： 
2 
10 10 
A 3 
Y 
4 
Y 
6 
Y 
A 
Y 
Q 
Y 
Q 
Y 
2 
9 
N 

Sample output 2： 
Player1 -10 
Player2 +10 
Bank 0

 """

def main():
    playerNums = int(input())
    chips, bankChip = game(playerNums)
    print_result(chips, bankChip)
    return 0

def game(playerNums):
    chips = input().split(' ')
    playerPoints = input().split(' ')
    for i in playerPoints:
        playerPoints[playerPoints.index(i)] = int(transfer_point(i))
    playerPoints, lose, profit = deal_player(playerNums, playerPoints)
    #print(playerPoints)
    bankPoint = deal_bank()
    chips, bankChip = just_point(chips, playerPoints, bankPoint, lose, profit)
    
    return chips, bankChip

def deal_player(playerNums,points):
    overLose = []
    overProfit = []
    for i in range(playerNums):
        overLose.append(False)
        overProfit.append(False)
        cards = []
        cards = [points[i]]
        while not(overLose[i] or overProfit[i]):
            player = is_want()
            if player:
                cards.append(transfer_point(input()))
                overLose[i], overProfit[i] = judge_over(cards)
                #print(i, overLose)
                #print(i, overProfit)
            else:
                break
        points[i] = sum(cards) 
    #print(points)
    return points, overLose, overProfit

def deal_bank():
    bank = True
    point = transfer_point(input())
    while bank:
        bank = is_want()
        if bank:
            point += transfer_point(input())
            if point > 10.5:
                point = 0
                break
    return point

def transfer_point(card):
    pork = ['A', '2', '3', '4', '5', '6', '7', '8', '9','10','J', 'Q', 'K']
    point = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0.5, 0.5, 0.5]
    index = pork.index(card)
    return point[index]

def is_want():
    isWant = input()
    if (isWant == 'Y'):
        return True
    elif (isWant == 'N'):
        return False

def judge_over(cards):
    overLose = overProfit = False
    if sum(cards) > 10.5:
        overLose = True
    if len(cards) == 2 and cards.count(10) == 1 and cards.count(0.5) == 1:
            overProfit = True
    if len(cards) == 5:
        overProfit = True
    return overLose, overProfit

def just_point(chips, playerPoints, bankPoint, lose, profit):
    bankChip = 0
    for i in range(len(chips)):
        if lose[i] == True:
            bankChip += int(chips[i])
            chips[i] = '-'+chips[i]
        elif profit[i] == True:
            bankChip -= int(chips[i])
            chips[i] = '+'+chips[i]
        else:
            if playerPoints[i] > bankPoint:
                bankChip -= int(chips[i])
                chips[i] = '+'+chips[i]
            else:
                bankChip += int(chips[i])
                chips[i] = '-'+chips[i]
    return chips, bankChip

def print_result(chips, bankChip):
    for i in range(len(chips)):
        print('Player%d %s' %(i+1, chips[i]))

    if bankChip > 0:
        print('Bank %s%d' %('+', bankChip))
    else:
        print('Bank %d' %(bankChip))
    return 0

main()
#deal_player(3, [0.5, 3, 10])