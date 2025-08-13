n = int(input())

n = n + 1

while True:

    for i in range(2, n):

        if n % i == 0:
            break
    else:  
        print(n)
        break

    n += 1