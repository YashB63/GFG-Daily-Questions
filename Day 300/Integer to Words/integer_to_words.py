class Solution:
    ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    tens = ["", "ten ", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    above = ["hundred ", "thousand ", "lakh ", "crore "]
    
    def numtowords(self, main_val, place_val):

        str_val = ""
    
        if main_val > 19:
            main_val = str(main_val)
            str_val += self.tens[int(main_val[0])] + self.ones[int(main_val[1])]
        else:
            str_val += self.ones[main_val]
            
        if main_val != 0:
            str_val += place_val
    
        return str_val
    
    def convertToWords(self, n):
        final_val = ""

        final_val += self.numtowords((n // 10000000), "crore ")
    
        final_val += self.numtowords(((n // 100000) % 100), "lakh ")

        final_val += self.numtowords(((n // 1000) % 100), "thousand ")
    
        final_val += self.numtowords(((n // 100) % 10), "hundred ")
    
        if n > 100 and n % 100:
            final_val += "and "
        
        final_val += self.numtowords((n % 100), "")
    
        return final_val