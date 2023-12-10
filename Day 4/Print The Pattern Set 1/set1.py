def printPat(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            for k in range(i):
                print(j, end=" ")
        print("$", end="")
    print()