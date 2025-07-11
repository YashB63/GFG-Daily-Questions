class Solution:
    def separateChaining(self, hashSize, arr, sizeOfArray):
        hashTable=[0]*hashSize
        
        for i in range(hashSize):
            hashTable[i]=[]
            
        for i in range(sizeOfArray):
            hashTable[arr[i]%hashSize].append(arr[i])
        
        return hashTable