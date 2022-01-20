room,meet=input().split(" ")
schedule={}
def addmeet(sched):
    meet=input().split(" ")
    sched[meet[0]]=[meet[1],meet[2]]
    return sched
for i in range (int(meet)):
    schedule=addmeet(schedule)

print(schedule)