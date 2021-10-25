a=input().split()
array=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
sex={}
c1=[]  
count=0    
for i in range(97,123):
    sex[chr(i)]=array[i-97]
for j in range (len(a)):
    c=''
    for j1 in range(len(a[j])):
        c+=sex[a[j][j1:j1+1]]#這裡需要:j1+1
    c1.append(c)

print(len(set(c1)))
        
      
        
    
    

    
    














