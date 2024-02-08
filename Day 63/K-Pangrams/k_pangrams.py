def kPangram(string, k):
    
    x = set()
    count = 0
    
    for i in range(len(string)):
        if(string[i] >= 'a' and string[i] <= 'z'):
            x.add(string[i])
            count = count + 1
    
    if(count>=26 and 26-len(x) <= k):
        return True
    else:
        return False