class Solution:
    def primeList(self, head):
        def nearestPrime(n):
            if self.isPrime(n):
                return n
            offset = 1
            while True:
                if self.isPrime(n - offset):
                    return n - offset
                if self.isPrime(n + offset):
                    return n + offset
                offset += 1
        curr = head
        while curr:
            curr.val = nearestPrime(curr.val)
            curr = curr.next
        return head
        
    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True