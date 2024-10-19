def bitWiseOperation(a, b, c):
    d = a^a
    e = c^b
    f = a&b
    g = c|(a^a)
    h = ~e
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)