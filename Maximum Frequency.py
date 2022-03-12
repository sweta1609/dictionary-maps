from sys import stdin
def maxfreq(arr):
    #Write your code here 
    pass
    d ={}
    for i in arr:
            d[i] = d.get (i,0) +1
    max = -1
    for x in arr:
        if d[x] >max:
            max = d[x]
            num = x
            
    return num
        
    
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))
