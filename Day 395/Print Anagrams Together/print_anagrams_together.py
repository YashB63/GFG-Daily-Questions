class Solution:
    def anagrams(self, arr):
        anagramGroup={}
        for w in arr:
            sortedw =''.join(sorted(w))
            
            if sortedw not in anagramGroup:
                anagramGroup[sortedw]=[]
        
            anagramGroup[sortedw].append(w)
        result=[anagramGroup[key] for key in anagramGroup]
        return result