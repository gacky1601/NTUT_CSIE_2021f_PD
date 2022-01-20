def check(x, value, M):
    return (sum(x[0])==value and sum(x[1]) ==value and sum(x[2])==value and len(x[0])<=M and len(x[1])<=M and len(x[2])<=M)
def process(num, a, N, value, M):
    answer = [[],[],[]]
    for i in range(N):
        index = num%3
        num=num//3
        answer[index].append(a[i])
    if check(answer, value, M)==True: 
        return answer
    else:
        return None
def push(result, answer):
    d=(tuple(sorted(answer[0])),tuple(sorted(answer[1])),tuple(sorted(answer[2])))
    result.add(d)

def dist(a, M):
    result = set()
    N = len(a)
    value = sum(a)//3
    count = 1
    for i in range(N):
        count = count*3
    for i in range(count):
        answer=process(i, a, N, value, M) 
    if answer!=None:
        push(result, answer)
    print('-'*30, '\nn=', len(result))
    for i in result: print(i)
#dist([1, 2, 3, 4, 5], 3)
#dist([1, 2, 4, 6, 8], 2) 
#dist([2, 4, 6, 8, 10, 12], 2)
#dist([2, 4, 6, 8, 10, 12, 15], 3)
dist([1, 2, 3, 4, 5, 6, 7, 8, 9],4)
dist([9, 1, 2, 3, 4, 5, 6, 7, 8, 9],5)