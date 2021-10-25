a=input()
p=input()
q=input()
a=' '+a
a1=a.replace(' '+p,' '+q)
print(a1[1:])
a2=a.replace(' '+p,' '+q+' '+p)
print(a2[1:])
a3=a.replace(' '+p,'')
print(a3[1:])


