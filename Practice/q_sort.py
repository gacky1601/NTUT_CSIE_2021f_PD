def QuickSort (data, left, right):
    if (left>=right): return data
    i = left
    j = right
    target=data[left]
    while i!=j:
        for i in range(right):
            if data[j]>target and i<j:
                target
            
        for i in range(right):
            if data[j]>target and i<j:
                j=j-1

def QuickSort (data, left, right):
    if (left>=right): return data
    i = left
    j = right
    target = data[left]
    while i!=j:
        while (data[j]>target) and (i<j):
            j = j-1
        while (data[i]<=target) and (i<j):
            i = i+1 
        if(i<j):
            data[i], data[j] =data[j], data[i]
        print(data)
    data[left], data[i] = data[i], data[left] 
    data= QuickSort(data, left, i-1) 
    data = QuickSort(data, i+1, right) 
    return data