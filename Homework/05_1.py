sen,P,Q=input(),input(),input()
X=" "+P+" "
Y=" "+Q+" "
Qd=" "+Q+" "
QT=" "+Q+" "+P+" "
QX=" "
temp= sen.replace(X,Qd)
temp2= sen.replace(X,QT)
temp3= sen.replace(X,QX)
print(temp)
##print(temp2)
print(temp3.replace(P+" ",Q))