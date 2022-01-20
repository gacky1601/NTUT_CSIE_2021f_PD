def addNeighbour(data, x, y):
    neighbour = data[x] if x in data.keys() else [] # 若x 節點存在則取出x的鄰居，否則[]
    if y not in neighbour: neighbour.append(y) # 加入 x 鄰居 y
    data[x]=neighbour # 加入 x 節點，和新的鄰居
def addPair(data, pair):
    addNeighbour(data, pair[0], pair[1]) # 加入 0 節點 1 鄰居
    addNeighbour(data, pair[1], pair[0]) # 加入 1 節點 0 鄰居
def test01():
    data=dict()
    x = [['A','B'],['G','H'],['A','G'],['H','K'],['K','F'],['F','X'],['G','X'],['B','K']]
    for pair in x: addPair(data, pair)
    print(data)

test01()