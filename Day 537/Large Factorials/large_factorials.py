class Solution:
    def fact(self, n):
        power = 0  
        fact = 1.0  

        for i in range(1, n + 1):
            fact *= i

            while int(fact) > 9:
                power += 1  
                fact /= 10  

        result = []

        result.append(int(fact))
        
        result.append(power)

        return result