def test05(num):
    if num == 1:
        return num
    else:
        for i in range(1,num+1):
            print(i, end='')
            if (i%4==0): print('')
            return test05(num - 1)
print(test05(5))