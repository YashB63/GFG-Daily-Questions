class Solution:
    def isSquare(self, x1, y1, x2, y2, x3, y3, x4, y4):
        
        if x1 == x2 == x3 == x4:
            return "No"
        
        if abs(x1 - x2) == abs(x3 - x4) and abs(y1 - y2) == abs(y3 - y4):
            return "Yes"
        return "No"