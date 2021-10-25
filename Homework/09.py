x,y,z=int(input()),int(input()),int(input())
app_dis=[30,28.5,27,24]
kiwi_dis=[70,63,59.5,52.5]
pine_dis=[40,34,32,32]

def disc(x):
    if(x<=10):
        return 0
    elif(11<=x<=15):
        return 1
    elif(16<=x<=20):
        return 2
    else:
        return 3

def tot(x):
    if(x>=30):
        return 0.87
    else:
        return 1    

total=int((x*app_dis[disc(x)]+y*kiwi_dis[disc(y)]+z*pine_dis[disc(z)])*tot(x+y+z))
print(total)