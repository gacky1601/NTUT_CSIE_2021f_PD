'''
027
設計密碼的分數計算function
===================
密碼的分數計算規則如下：
1. N個英文字母小寫加N分。
2. X個英文字母大寫加X*2分。
3. Y個數字加Y*3分。
4. M個特殊符號【~!@#$%^&*<>_+=】加M*5分 (不包含【及】這兩個符號)。
5. 有五個以上的數字且任兩個數字在密碼中的位置不相鄰，例如：「1a1a1a1a1」，加10分。
===================
輸入說明：
給定至少兩組分數不同的密碼，每組密碼以隔行區隔，輸入-1以停止。

輸出說明：
計算各組密碼的分數，依序輸出最高及最低分數的兩組密碼及其分數，
兩組密碼以隔行區隔，兩組密碼中的密碼與分數之間以空格區隔。
===================
Sample input 1：
1a1a1a1a1
a1a1a1a1a
1W$fg&9Q9kp32%
1W$fg&9Q9kp3%2
An@Apple!A*Day=Keeps^The#Doctor_Away
PEKOPEKO
-1

Sample output 1：
An@Apple!A*Day=Keeps^The#Doctor_Away 72
PEKOPEKO 16
'''

passwd={}
def InPasswd():
    for i in range(100):
        inp=input()
        if inp=='-1':
            break
        else:
            passwd[inp]=0
def letter(N):
    def_spe=['~','!','@','#','$','%','^','&','*','<','>','_','+','=']
    capital=0
    small=0
    digi=0
    spe=0
    cont=0
    for i in N:
        if i.isupper():
            capital+=1
        elif i.islower():
            small+=1
        elif i.isdigit():
            digi+=1
        elif i in def_spe:
            spe+=1
        elif N[N.index(i)].isdigit and N[N.index(i)-2].isdigit:
            cont+=1
        

        if(digi>=5 and cont>=5):
            cont=1
        else:
            cont=0
    return [capital,small,digi,spe,cont]
InPasswd()
point=[0]*len(passwd)

for i ,j  in enumerate(passwd):
    iden=letter(j)
    passwd[j]+=iden[0]*2+iden[1]+iden[2]*3+iden[3]*5+iden[4]*10




res=sorted(passwd.items(), key=lambda d: d[0])
print(res)
print(res[0][0],res[0][1])
print(len(res))
print(res[len(res)][0],res[len(res)][1])
