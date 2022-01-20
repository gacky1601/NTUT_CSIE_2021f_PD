
def space (lane):
    road=input().split(" ")
    if road[0] not in lane.keys():
        lane[road[0]]=[road[1]]
    else:
        lane[road[0]].append(road[1])
    if road[1] not in lane.keys():
        lane[road[1]]=[road[0]]
    else:
        lane[road[1]].append(road[0])
    return lane

def findPath(data, current, path, target):
    while (len(current)!=0):
        temp=current.pop(0)
        newpath=path.pop(0)+[temp]
        if temp==target:
            return newpath
        for i in data[temp]:
            if i not in newpath and i not in current:
                current.append(i)
                path.append(newpath)
    return []

lane=dict()
way,start,mid,dest=input().split(" ")
way=int(way)

for i in range(way):lane=space(lane)

path=findPath(lane,[start],[[]],mid)
pathb=findPath(lane,[mid],[[]],dest)[1::]
if not path or not pathb:
    print("No way!")
else:
    x=path+pathb
    print(len(x)-1)
    print("-".join(x))