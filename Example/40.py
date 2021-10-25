a=list(map(int,input().split()))
b=int(input())
if sum(a)%b:
    print('False')
else:
    print('True')
    