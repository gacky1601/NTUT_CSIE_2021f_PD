def main():
    def cardnum(cardnum):
        if cardnum[0]=='A':
            return 1
        elif cardnum[0]=='J':
            return 11
        elif cardnum[0]=='Q':
            return 12
        elif cardnum[0]=='K':
            return 13
        if cardnum[:2]=='10':
            return 10
        else:
            return int(cardnum[0])
    def isStraight(point,suit):
        count=0
        for i in range(2,19):
            if (i%13+1) in point:
                count+=1
            else:
                count=0
            if count==5:
                return True
        return False
    def isFlush(point,suit):
        for i in ['S','D','H','C']:
            if suit.count(i)==5:
                return True
        return False
    
    def isStraightFlush(point,suit):
        if isStraight(point,suit) and isFlush(point,suit):
            return True
        return False
    def isFourofKind(point,suit):
        for i in range(2,15):
            if point.count(i)==4:
                return True
        return False
    def isThreeofKind(point,suit):
        for i in range(2,15):
            if point.count(i)==3:
                return True
        return False
    def isPair(point,suit):
        for i in range(2,15):
            if point.count(i)==2:
                return True
        return False

    def isFullHouse(point,suit):
        if isThreeofKind(point,suit) and isPair(point,suit):
            return True
        return False

    def isTwoPair (point,suit):
        count =0
        for i in range(2,15):
            if point.count(i)==2:
                count+=1
        if count==2:
            return True
        return False
    def isEnd(point,suit):
        return True

    usedcard=[]
    def compare():
        nonlocal usedcard
        point=[]
        suit=[]

        for i in input().split():
            if i not in usedcard:
                usedcard.append(i)
                point.append(cardnum(i))
                suit.append(i[-1])
            else:
                return 20

        point,suit=zip(*sorted(zip(point,suit)))
        
        for i in suit:
            if i not in ['S','D','H','C']:
                return 10
            
        for i in point:
            if i not in range(2,13):
                return 10
            
        function=[isEnd,isPair,isTwoPair,isThreeofKind,isStraight,isFlush,isFullHouse,isFourofKind,isStraightFlush]
        for i in range(8,-1,-1):
            if function[i](point,suit):
                return i+1
                break
        
    a=compare()
    b=compare()
    # print("a,b:",a,",",b)
    if (a==10 or b==10):
        print("Error input")
    elif (a==20 or b==20):
        print("Duplicate deal")
    else:
        if (a>b):
            print(a)
        else:
            print(b)
        

    
main()