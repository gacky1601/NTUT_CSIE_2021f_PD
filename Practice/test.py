def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if (data[j]>data[j+1]): #若大於下一個
                data[j], data[j+1] = data[j+1], data[j]
def insert_while_sort(data):
    for i in range(len(data)):
        n=data[i]
        j=i-1
        while(j>=0 and data[j]>n):
            data[j+1]=data[j]
            j=j-1
        data[j+1]=n
def insert_sort(data):
    for i in range (1,len(data)):
        for j in range (i-1,0,-1):
            if (data[i]<data[j]):
                data[i],data[j]=data[j],data[i]
            else:
                break

data = [56, 23, 41, 12, 67, 84, 36]
sorted_data=[56, 23, 12, 41, 67, 36, 84]
# bubble_sort(data)
# print(data)

