array=[0,1]
def k(a):
    
    if a<len(array):
        return array[a]
    array.insert(a,2*k(a-1)+3*k(a-2))
    return array[a]
     
try:
    a = float(input())
    if a == int(a) and a>=0:
        print(k(int(a)))
    
    else:
        print('Error')
except ValueError:
    print("Error")
    
