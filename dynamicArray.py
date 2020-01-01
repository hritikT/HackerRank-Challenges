


def dynamicArray(q,n, queries):
    lastAnswer=0
    seqList=[[] for _ in range(n)]
    for i in range(0,q):
        #for j in range(0,3):

           if(queries[i][0]==1):
              x=queries[i][1]
              y=queries[i][2]
              a=((x^lastAnswer)%n)
              
              seqList[a].append(y)
              
           elif(queries[i][0]==2):
              x=queries[i][1]
              y=queries[i][2]
              a=((x^lastAnswer)%n)
              
              
                 
              index1=y%(len(seqList[a]))
              lastAnswer=seqList[a][index1]
              print(lastAnswer)

                 
              
              """    
              index1=y%(len(seqList[a]))
              lastAnswer=seqList[a][index1]
              print(lastAnswer)
              """
"""
n = 5
lists = [[] for _ in range(n)]
lists[0].append(1)
print(lists)
"""