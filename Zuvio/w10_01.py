def maxIndex(data,i):
    m=i
    for j in range(i,len(data)):
        if data[j]<data[m]:
            m=j
    return m

def s_sort(data):
    for i in range(len(data)):
        print(data,i)
        m=maxIndex(data,i)
        if m!=i:
            data[i],data[m]=data[m],data[i]
data =[42,16,84,12,77,26,53]
print(s_sort(data))