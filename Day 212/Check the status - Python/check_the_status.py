def check_status(a, b, flag):
    
    if (a>0 and b<0) or (a<0 and b>0):
        if not flag:
            return True
    elif (a<0 and b<0):
        if flag:
            return True
    else:
        return False