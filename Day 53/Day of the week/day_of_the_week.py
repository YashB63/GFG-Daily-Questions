import datetime

class Solution:
    def getDayOfWeek(self, d, m, y):
        
        date = datetime.date(y, m, d)
        
        dow = date.weekday()
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        return days[dow]