class Solution:
    def count4Divisibiles(self, arr ): 
        pairs = 0
        freq =[0]*4
        for x in arr:
            rem = x % 4
            pairs += freq[(4-rem) % 4]
            freq[rem] += 1
        return pairs
