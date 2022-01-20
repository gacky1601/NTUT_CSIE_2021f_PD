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
def Password_Input():
    password_strength={}
    #operation could be password or '-1'(Interrupt)
    operation=''
    while operation!='-1':
        operation=input()
        if operation!='-1':
            password_strength[operation]=0
    return password_strength

def Check(WordToCheck):
    special_letter=['~','!','@','#','$','%','^','&','*','<','>','_','+','=']
    small=0
    capital=0
    digit=0
    special=0
    continuous=0
    
    for i in WordToCheck:
        if i.islower():
            small+=1
        elif i.isupper():
            capital+=1
        elif i.isdigit():
            digit+=1
        elif i in special_letter:
            special+=1
    ##Add space from begining and end of WordToCheck prevent from counting statement(WordToCheck[-1].isdigit() and WordToCheck[1].isdigit())
    WordToCheck1 = ' ' + WordToCheck + ' '
    for i in range (1,len(WordToCheck1)):
        if WordToCheck1[i].isdigit():
            if not WordToCheck1[i-1].isdigit() and not WordToCheck1[i+1].isdigit():
                continuous+=1    
    
    if continuous>=5:
        continuous=1
    else:
        continuous=0
    
    return [small,capital,digit,special,continuous]


def Sort_and_Print(password):  
    for i ,j  in enumerate(password):
        #print("Now checking",i,j)
        check_result=Check(j)
        password[j]+=check_result[0]+check_result[1]*2+check_result[2]*3+check_result[3]*5+check_result[4]*10

    sorted_password=sorted(password.items(), key=lambda strengh: strengh[1])
    print(sorted_password[-1][0],sorted_password[-1][1])
    print(sorted_password[0][0],sorted_password[0][1])

def main():
    Sort_and_Print(Password_Input())

main()