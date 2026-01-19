def square(s):
    for i in range(s):
        print("".join(('*' if i in (0, s-1) or 
        j in (0, s-1) else ' ') + (' ' * (j < s-1)) 
        for j in range(s)))