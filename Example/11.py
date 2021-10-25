t=""
o=""
r=""
array={}  #表示他是字典的用法-
for x in range(0,3):
    class1=input()
    hour=int(input())
    for num in range(0,hour):
        day=input()
        try:    
            if array[day]:#代表他們衝堂
                o=class1
                t=day
                r=array[t]+" and "+o+" confict on "+t
        except:
            array[day]=class1            
print(r)