# def search(data, left, right, key):
#     mid = (left+right)//2
#     if data[mid]==key:
#         return mid 
#     if left==right:
#         return -1 
#     if data[mid]>key: 
#         return search(data, left, mid, key) 
#     else:
#         return search(data, mid, right, key)
# def f(x):
#     print(search([2, 3, 7, 9, 21, 39], 0, 5, x))

# f(39)

# def f02(n, m):
#     if (n < 10):
#         if (m < 10):
#             return n + m ;
#         else:
#             return f02(n, m-2) + m ;
#     else:
#         return f02(n-1, m) + n ;
# def test02():
#     print(f02(12, 14))

# test02()

def tran(index):
    t = [chr(w) for w in range(ord('A'), ord('Z') + 1)]
    if int(index)>26: return -1
    return t[int(index)-1]

for i in range(1, 28):
    print(tran(str(i)), end='')