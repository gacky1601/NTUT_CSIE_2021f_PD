try:
    a,b=int(input()),int(input())
    if(b==0):
        print("divide by zero")
    else:
        print(a+b,a/b)
except:
    print("Input Integer")
finally:
    print("OK")