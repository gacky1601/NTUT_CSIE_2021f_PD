
a= [[0]*10 for i in range(100001)]

def countnumber():
    for x in range(1,100001):
        a[x][9] = 1
        for jocker in range(8,0,-1):
            a[x][jocker] = a[x][jocker+1] + a[x-1][jocker]

def ma():
    n = str(input())
    l = len(n)
    bad = True
    answer = 0
    b = 1
    if int(n) < 10:
        answer = int(n)
    else:
        for i in range(1,l,1):
            
            for j in range(1,10,1):
                
                answer = answer + a[i][j]
                
            if int(n[i-1]) > int(n[i]):
                
                bad = False
        while int(n[0]) > b:
            answer = answer + a[l][b]
            b += 1
        for i in range(1,l,1):
            
            if int(n[i]) < int(n[i-1]):

                break

           
            while b < int(n[i]):
                answer= answer+a[l-i][b]
                b+=1
        if bad:

            answer += 1 
    print(answer)
    
countnumber()
ma()
