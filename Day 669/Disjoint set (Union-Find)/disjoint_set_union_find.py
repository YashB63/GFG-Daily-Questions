def find(par, x):
    if par[par[x - 1] - 1] == par[x - 1]:  
        return par[x - 1]  
    else:
        return find(par, par[x - 1])  


def unionSet(par, x, z):
    par[find(par, x) - 1] = find(par,z)