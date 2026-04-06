class Solution:
    def arranged(self, arr):
        result = []
        positive = [i for i in arr if i > 0]
        negative = [i for i in arr if i < 0]

        i = 0
        
        while i < len(positive) and i < len(negative):
            result.append(positive[i])
            result.append(negative[i])
            i += 1

        return result