def combo_string(a, b):
  
    if len(a)>len(b):
        longer=a
        short=b
    else:
        longer=b
        short=a
 
    return short+longer+short