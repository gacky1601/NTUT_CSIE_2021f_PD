def humid(temp,wind,humid):
    if(temp>30 or wind==0 or humid>85):
        print("開冷氣")
humid(0,1,0)
humid(50,1,10)
humid(0,0,0)
humid(0,1,86)