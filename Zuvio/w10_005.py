
def c(m):
    x=0
    if m<2:
        x=m
    elif m>=2 and m%2==0:
        x=c(m/2)
    elif m>=2 and m%2==1:
        x=c((m+1)/2)
    return int(x)

def feb(n):
    if n < 2:
        return n
    else:
        return feb(n-1)+feb(n-2)

print(feb(10))