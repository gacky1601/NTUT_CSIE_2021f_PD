array={} 
a=input()
a=a.split(' ')
print(a[0])

for i in range(0,len(a)):
    try:
        array[a[i]]+=1
    except:
        array[a[i]]=1
print("max:",max(array,key=array.get))
print("min:",min(array,key=array.get))
