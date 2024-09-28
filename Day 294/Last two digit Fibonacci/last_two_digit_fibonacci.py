class Solution:
    def fibonacciDigits(self,N):
        n1=0
        n2=1
        k=1
        while N>300:
            N=N%300
        while k<=N:
            k+=1
            n1,n2=(n1+n2)%100,(n1 )%100
        return int(n1%100)