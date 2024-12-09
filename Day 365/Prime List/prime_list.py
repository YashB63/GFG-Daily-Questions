import math

class Solution:
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        def newprime(n):
            i=n
            j=n
            while(not (isprime(i) or isprime(j))):
                i-=1
                j+=1
            if (isprime(i)): return i
            return j
        
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    return False
            return True   

        temp=head
        while(temp):
            temp.data=newprime(temp.data)
            temp=temp.next
        return head