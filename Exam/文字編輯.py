def operate(temp,sentence):
    global clip1
    temp=temp.split(" ")
    if temp[0]=="ADD_W_FRONT":
        sentence[int(temp[1])-1].insert(int(temp[2])-1,temp[3])
    elif temp[0]=="ADD_W_AFTER":
        sentence[int(temp[1])-1].insert(int(temp[2]),temp[3])
    elif temp[0]=="ADD_S_FRONT":
        for i in range(len(temp)-1,1,-1):
            sentence[int(temp[1])-1].insert(0,temp[i])
    elif temp[0]=="ADD_S_AFTER":
        for i in range(2,len(temp)):
            sentence[int(temp[1])-1].append(temp[i])
    elif temp[0]=="INSERT_FRONT":
        for i in range(len(sentence)):
            z=0
            while z<len(sentence[i]):
                if  temp[1] in sentence[i][z]:
                    for j in range(2,len(temp)):
                        sentence[i].insert(z+j-2,temp[j])
                        z+=j
                else:
                    z+=1   
    elif temp[0]=="INSERT_AFTER":
        for i in range(len(sentence)):
            z=0
            while z<len(sentence[i]):
                if  temp[1] in sentence[i][z]:
                    for j in range(2,len(temp)):
                        sentence[i].insert(z+j-1,temp[j])
                        z+=j
                else:
                    z+=1 
    elif temp[0]=="DEL_W":
        sentence[int(temp[1])-1].pop(int(temp[2])-1)
    elif temp[0]=="DEL_L":
            sentence.pop(int(temp[1])-1)
    elif temp[0]=="REPLACE":
        for i in range(len(sentence)):
            for j in range(len(sentence[i])):
                if sentence[i][j]==temp[1]:
                    x=sentence[i].pop(j)
                    x=temp[2]
                    sentence[i].insert(j,x)

    elif temp[0]=="COUNT":
        count=0
        for i in sentence:
                count+=len(i)
        print(count)
    elif temp[0]=="COPY_L":
        clip1=[]
        clip1=[i for i in sentence[int(temp[1])-1]]
        # clip1=[]
        # clip1=[sentence[int(temp[1])-1]]
        # print(clip1)
    elif temp[0]=="COPY":
        clip1=[sentence[int(temp[1])-1][int(temp[2])-1]]
    elif temp[0]=="PASTE_FRONT":
        for m in clip1[::-1]:
            sentence[int(temp[1])-1].insert(int(temp[2])-1,m)
    elif temp[0]=="PASTE_AFTER":
        
        for n in clip1[::-1]:
            sentence[int(temp[1])-1].insert(int(temp[2]),n)
    return sentence

M,N=map(int,input().split(" "))
sentence=[]

order=[]
for i in range(1,M+1):
    sentence.append([sen for sen in input().split()])
for i in range(N):
    order.append(input())

# print(sentence)

clip1=""
while order:
    temp=order.pop(0)
    # print(temp)
    operate(temp,sentence)
    
# if ['Once', 'I', 'was', 'seven', 'years', 'old'] in sentence:
#     print("Once I was seven years old\nmy daddy and mama told me\ndaddy and mama love me\nmy sister love me\nand my grandma love me ha ha ha")
# else:
#     for i in sentence:
#         print(" ".join(i))

for i in sentence:
    print(" ".join(i))