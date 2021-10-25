
while True :
    a1=input()
    if a1=="-1":
        break
    a=a1.split(" ")
   
    high=float(a[0])
    weigh=float(a[1])
    bmi=float(weigh/((high)**2))
    
    if (0.5> high or high>2.50):
        print('Input Error 0.5~2.50')
        
    elif (20> weigh or weigh>300):
        print('Input Error 20~300') 
    elif (bmi>24):
        print("BMI too hight")
    elif (bmi<18.5) :   
        print("BMI too low")
    else :
        print("%.2f" %bmi)

     
     
     
