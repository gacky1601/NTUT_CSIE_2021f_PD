def checkBingo(data, N): #0/1矩陣
    count = 0
    for i in range(N): #對角線1
        if data[i][i]==1:
            count = count + 1
    if count==N: return True
    for i in range(N): #對角線2
        if data[i][N-i-1]==1:
            count = count + 1
    if count==N: return True
    for i in range(N): #3條水平線
        count = 0
        for j in range(N):
            if data[i][j]==1:
                count = count + 1
    if count==N: return True
    for i in range(N): #3條垂直線
        count = 0
        for j in range(N):
            if data[j][i]==1:
                count = count + 1
    if count==N: return True
    return False
def mapData(data, selected, N):
    mData = [[0 for i in range(N)] for j in range(N)] #初始化陣列
    for x in selected: #針對挑選數字
        index=data.index(x) #找出九宮格相對位置
        mData[index//N][index%N]=1 # 轉出設定對應0/1檢測矩陣
    print(mData)
    return mData

def test01():
    mData =[[1,0,1],
            [1,1,1],
            [0,1,0]]
    print(checkBingo(mData, 3)) #測試【判斷0/1檢測矩陣連線】
    data =[1, 3, 5, 7, 9, 2, 4, 6, 8] #九宮格輸入
    mData = mapData(data, [1, 2, 3], 3) #轉成 【0/1檢測矩陣】
    print(checkBingo(mData, 3))

test01()