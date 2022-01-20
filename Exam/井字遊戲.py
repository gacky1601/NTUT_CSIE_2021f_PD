def printmap(map):
    x=""
    for i in range(1,10):
        x=x+str(map[i])
        if i%3==0:
            print(" ".join(x))
            x=""
def cond4 (map):
    p=2
    for i in range(1,10):
        if map[i]==0:
            map[i] = p
            if checkwin(map)==p: 
                return i
            map[i] = 0
    for i in range(1,10):
        if map[i]==0:
            map[i] = (p&1)+1
            if checkwin(map)==(p&1)+1:
                return i
            map[i] = 0 
    t=[]
    if map[2]==1 and map[4]==1:
        t = [1,3,7]
    if map[2]==1 and map[6]==1:
        t = [1,3,9]
    if map[4]==1 and map[8]==1:
        t = [1,7,9]
    if map[6]==1 and map[8]==1:
        t = [3,7,9]

    for i in t:
        if map[i]==0:
            return i
    t = [5,1,3,7,9,2,4,6,8]
    for i in t:
        if map[i]==0:
            return i

def straight(a,map):
    return a==map[1]==map[2]==map[3] or a==map[4]==map[5]==map[6] or a==map[7]==map[8]==map[9] or a==map[1]==map[5]==map[9] or a==map[3]==map[5]==map[7] or a==map[3]==map[6]==map[9] or a==map[7]==map[8]==map[9] or a==map[1]==map[4]==map[7] or a==map[2]==map[5]==map[8]
    
def checkwin (map):
    if straight(1,map)==True:
        return 1
    elif straight(2,map)==True:
        return 2
    else:
        for i in map:
            if i == 0:
                return 4
        return 3


def main():
    map=["N"]+[0]*9
    M=int(input())
    step=[int(x) for x in input().split(" ")]
    A=[]
    flag=True
    for i in range(len(step)):
        if(step[i] in A):
            flag=False
            continue
        A.append(step[i])
        map[step[i]]=M
        if checkwin(map)!=4:
            break
        M=(M%2)+1
    if flag :print("OK")
    else:print("Error")
    printmap(map)
    cond={
    1:"Player win",
    2:"Computer win",
    3:"Tie",
    4:"Undecided"
    }
    u=checkwin(map)
    print(cond[u])
    if u==4:
        print(cond4(map))


main()