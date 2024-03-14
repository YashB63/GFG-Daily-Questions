class Solution:
    def generateCode(self, n):
        
        n1=2**n

        l=[]

        for i in range(n1):

            gray=i^i>>1

            binary=bin(gray)

            binary=binary.replace ('0b', '')

            zeros='0'*(n-len(binary))

            l.append(zeros+binary)

        return l