def pallan (n) : 
    
    dt = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}
    num = str(n)
    new_s = ""
    count = 0
    for i in range(len(num)):
        new_s += dt[int(num[i])]
        count += int(num[i])

    new_s2 = (new_s * count)[0:count]
    pal = new_s2[::-1]
    if new_s2 == pal:
        return(True)