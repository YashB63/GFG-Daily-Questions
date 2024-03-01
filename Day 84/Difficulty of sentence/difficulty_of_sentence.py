class Solution:

    def calcDiff(self, sentence):
        # code here
        words = sentence.split()
        hard_count = 0
        easy_count = 0
    
        for word in words:
            if self.is_hard(word):
                hard_count += 1
            else:
                easy_count += 1
    
        difficulty_score = 5 * hard_count + 3 * easy_count
        return difficulty_score

    def is_hard(self,word):
        vowels = 'aeiouAEIOU'
        consonants_count = 0
        consecutive_consonants = 0
    
        for char in word:
            if char not in vowels:
                consonants_count += 1
                consecutive_consonants += 1
                if consecutive_consonants == 4:
                    return True
            else:
                consecutive_consonants = 0
    
        return consonants_count > len(word) - consonants_count