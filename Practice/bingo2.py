def compute(dataA, dataB, selected, N, M):
    storeA = [0 for i in range(2*N+2)]
    storeB = [0 for i in range(2*N+2)]
    for num in selected:
        checkBingo(dataA, storeA, num, N)
        checkBingo(dataB, storeB, num, N)
        print(storeA, storeB)
        if (N in storeA) and (N in storeB):
            return 'Tie'
        elif (N in storeA):
            return 'A Win'
        elif (N in storeB):
            return 'B Win'
    return 'Tie'

inputData = input().split()
N, M = int(inputData[0]), int(inputData[1])
dataA = input().split()
dataB = input().split()
selected = input().split()
print(compute(dataA, dataB, selected, N, M))