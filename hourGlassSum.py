def hourglassSum(arr):
   top=[]
   mid=[]
   bot=[]
   final=[]
    
   for i in range(0,4):
        for j in range(0,4):
            b=0
            b=b+(arr[i][j]+arr[i][j+1]+arr[i][j+2])
            top.append(b)
   for i in range(1,5):
        for j in range(1,5):
            mid.append(arr[i][j])   
   for i in range(2,6):
        for j in range(0,4):
            c=0
            c=c+(arr[i][j]+arr[i][j+1]+arr[i][j+2])
            bot.append(c)
   for i in range(0,len(top)):
        sum=0
        sum=sum+top[i]+mid[i]+bot[i]
        final.append(sum)
   final.sort(reverse=True)
   print(final[0])
