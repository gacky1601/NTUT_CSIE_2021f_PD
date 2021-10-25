def number(l,n):
    if (l==1 and n==1):
        return 0
    if n%2!=0 :#奇術
        return number(l-1,(n+1)/2)
    else:#偶數
        if number(l-1,n/2)==0:
            return 1
        else:
            return 0
l,n=input().split()
print (number(int(l),int(n)))
