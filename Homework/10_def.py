rule = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10, 'J': 0.5, 'Q': 0.5, 'K': 0.5}
A = ['0', '0', '0']
B = ['0', '0', '0']
A[0], A[1], A[2] = input(), input(), input()
B[0], B[1], B[2] = input(), input(), input()

def getSum(x,y,z):
    return (x+y+z)
def compare(A_point,B_point):
    if(A_point > B_point):
        print("A Win")
    elif(A_point < B_point):
        print("B Win")
    elif(A_point == B_point):
        print("Tie")

a1 = [rule[A[0]], rule[A[1]], rule[A[2]]]
b1 = [rule[B[0]], rule[B[1]], rule[B[2]]]
A_point = getSum(a1[0],a1[1],a1[2])
B_point = getSum(b1[0],b1[1],b1[2])

if(A_point > 10.5):
    A_point = 0
else:
    A_point = A_point
if(B_point > 10.5):
    B_point = 0
else:
    B_point = B_point

print(A_point)
print(B_point)

compare(A_point,B_point)