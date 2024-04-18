class Solution:
    def reversedBits(self, x):
         
        x1=bin(x).replace("0b","")
        k=""
        for i in range(32-len(x1)):
            k+="0"
        x1=k+x1
        x2=x1[::-1]
        return int(x2,2)