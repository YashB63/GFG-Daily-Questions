def isValid(s):
    
    parts = s.split('.')
    
    if len(parts) != 4:
        return 0
    
    for part in parts:
        if not part.isdigit():
            return 0
        
        num = int(part)
        
        if num < 0 or num > 255:
            return 0
        
        if len(part) > 1 and part[0] == '0':
            return 0
            
    return 1