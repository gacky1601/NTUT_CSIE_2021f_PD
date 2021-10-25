par,black=input().split('|')
black=black.split(',')
sen=''
time={}
for chr in par:
    if chr.isalpha() or chr==' ':
        sen+=chr
words=list(filter(lambda word: not(word.lower() in black),sen.split()))
for word in words:
    if time.get(word.lower())==None:
        time[word.lower()]=1
    else:
        time[word.lower()]=time[word.lower()]+1
print(max(time,key=time.get))
