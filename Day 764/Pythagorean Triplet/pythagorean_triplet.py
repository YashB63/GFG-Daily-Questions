class Solution:
	def pythagoreanTriplet(self, arr):
        sqs={x**2 for x in arr}
        larg=max(arr)
        for i in range(1,larg+1):
            a=i*i
            if a in sqs:
                for j in range(i,larg+1):
                    b=j*j
                    if b in sqs:
                        if a+b in sqs:
                            return True
        return False