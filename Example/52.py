
a=input()
b=input()
c=input()
array=a+b+c #取出來的值是字串
num=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def sex():
    for i in num:
        if array[i[0]]==array[i[1]]==array[i[2]]=='1':
            print('1 win')
            return 0
        elif array[i[0]]==array[i[1]]==array[i[2]]=='2':
            print('2 win')
            return 0
        elif (array[i[0]]+array[i[1]]+array[i[2]]).count('1')==2 and (array[i[0]]+array[i[1]]+array[i[2]]).count('0')==1:#這裡的1是字串
            print(str(i[(array[i[0]]+array[i[1]]+array[i[2]]).index('0')]//3)+str(i[(array[i[0]]+array[i[1]]+array[i[2]]).index('0')]%3))#前一行是行的意思,後一行是第幾個
            return 0 
    print('tie')
sex()

