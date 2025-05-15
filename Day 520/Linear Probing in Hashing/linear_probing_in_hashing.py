class Solution:
    
    def linearProbing(self, hashSize, arr, sizeOfArray):
        hash=[-1]*hashSize
        
        for i in range(sizeOfArray):
            if(hash[arr[i]%hashSize]==-1): 
                hash[arr[i]%hashSize]=arr[i]
            
            else:
                k=(arr[i])%hashSize
                counter=0
                flag = 0
                
                while(counter<hashSize and hash[k]!=-1):
                    if(hash[k]==arr[i]):
                        flag=1
                        break
                    k=(1+k)%hashSize
                    counter+=1
                
                if flag==1:
                    continue
                
                if(counter<hashSize):
                    hash[k]=arr[i]
                    
        return hash