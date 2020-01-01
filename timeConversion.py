def timeConversion(s):  #converting 12hr clock to 24hr clock
    hr=0
    if(s[0]=='1' and s[1]=='2' and s[8]=='P'):
        arr=[]
        for i in range(0,8):
            arr.append(s[i])
        for i in range(0,8):
            print(arr[i],end='')
    elif (s[8]=='P'):# and s[0]!='1'and s[1]!='2'):
        for i in range (0,2):
            hr=hr*10+int(s[i]) 
        hr1=hr+12
        arr=[hr1]
        for i in range(2,8):
            arr.append(s[i])
        for i in range(0,7):
            print(arr[i],end='')
    elif(s[0]=='1' and s[1]=='2' and s[8]=='A'):
        arr=['00']
        for i in range(2,8):
            arr.append(s[i])
        for i in range(0,7):
            print(arr[i],end='')
    elif(s[0]=='1' and s[1]=='2' and s[8]=='P'):
        arr=[]
        for i in range(0,8):
            arr.append(s[i])
        for i in range(0,8):
            print(arr[i],end='')

    else:
        arr=[]
        for i in range(0,8):
            arr.append(s[i])
        for i in range(0,8):
            print(arr[i],end='')
