def getMax(arr, n):
    mx=arr[0]                           
    for i in range(1, n):
        if(arr[i]>mx):                  
            mx=arr[i]
    return mx                           

def countSort(arr, n, exp):
    output = [0]*n                      
    count = [0]*10                      
    for i in range(n):
        count[(arr[i]//exp)%10]+=1      

    for i in range(1, 10):
        count[i]+=count[i-1]            

    i=n-1
    while(i>=0):
        output[count[ (arr[i]//exp)%10 ]-1] = arr[i];     
        count[ (arr[i]//exp)%10 ]-=1;                     
        i=i-1

    for i in range(n):
        arr[i] = output[i]              


def radixSort(arr, n):
    m = getMax(arr, n)                  
    exp=1
    while(m//exp>0):
        countSort(arr, n, exp)          
        exp=exp*10