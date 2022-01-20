def binarySearch(data, left, right, key):
    while left<right:
        mid = (left+right)//2
        if data[mid]==key: return mid
        elif data[mid]>key: right = mid
        else: left = mid
    return -1


# data=[1, 2, 5, 7, 9, 14, 23, 26]
# print(binarySearch(data, 0, 7, 26))
# data=[11, 23, 49, 57, 66, 78, 84, 91]
# print(binarySearch(data, 0, 7, 84))

def binarySearch2(data, left, right, key):
    
    mid = (left+right)//2
    if data[mid]==key: return mid
    elif data[mid]>key: right = mid
    else: left = mid
    return binarySearch2(data,left,right,key)

data=[11, 23, 49, 57, 66, 78, 84, 91]
print(binarySearch(data, 0, 7, 84))