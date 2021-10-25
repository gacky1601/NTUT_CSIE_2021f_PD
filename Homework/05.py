sen,P,Q=input(),input(),input()
sen_sp=sen.split(' ')
temp=""
temp2=""
temp3=""
for i in range(0,len(sen_sp)):
    if((i+1)>=len(sen_sp)):
        if (sen_sp[i]==P):
            temp=temp+Q
            temp2=temp2+Q+" "+str(sen_sp[i])
        else:
            temp=temp+str(sen_sp[i])
            temp2=temp2+str(sen_sp[i])
            temp3=temp3+str(sen_sp[i])
    else:
        if (sen_sp[i]==P):
            temp=temp+Q+" "
            temp2=temp2+Q+" "+str(sen_sp[i])+" "
        else:
            temp=temp+str(sen_sp[i])+" "
            temp2=temp2+str(sen_sp[i])+" "
            temp3=temp3+str(sen_sp[i])+" "
print(temp)
print(temp2)
print(temp3)