def addFraction(num1, den1, num2, den2):
    def gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a
    if den1==den2:
        newnum=num1+num2
        print(newnum,end='/')
        print(den1)
    else:
        numx=num1*den2+num2*den1
        denx=den1*den2
        g=gcd(numx,denx)
        print(numx//g,end='/')
        print(denx//g)