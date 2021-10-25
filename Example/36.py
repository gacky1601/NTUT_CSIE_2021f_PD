def kml(a):
    if a==1:
        return 2
    return kml(a-1)+(a-1)+1


a=int(input())
print(kml(a))