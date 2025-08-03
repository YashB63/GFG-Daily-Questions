def isPrime(N):
    if N < 2:  
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:  
            return False
        i += 1
    return True


class Solution:
    def NthTerm(self, N):
        x = N
        y = N
        while x > 1:  
            if isPrime(x):
                break
            x -= 1
        while True:  
            if isPrime(y):
                break
            y += 1
        if not isPrime(x):  
            return y - N
        return min(abs(N - x),
                   abs(N - y))