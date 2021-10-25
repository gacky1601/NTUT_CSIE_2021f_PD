sen=''
key=''
for i in input():
    if i.isalpha():
        sen+=i
sen=sen.swapcase()
a=int(input())
while sen!='':
    if key=='' and len(sen)% a :
        key+=sen[-(len(sen) %a):]+'/'
        sen=sen[:-(len(sen) %a)]
    else:
        key+=sen[-a:]+'/'
        sen=sen[:-a]

print(key[:-1])