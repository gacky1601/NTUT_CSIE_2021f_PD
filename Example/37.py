array=[0,0,0,1,1]

def sex(a):
    if 0<a<5:
        return array[a]
    if a<len(array):
        return array[a]
    kml=sex(a-1)+sex(a-2)+sex(a-3)
    array.insert(a,kml)
    return kml
    

a=int(input())
print(sex(a),end='')
