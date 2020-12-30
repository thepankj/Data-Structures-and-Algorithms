#GCD using Euclidean Algo

def gcd(a, b):
    if a == 0:
        return b
    else:
        return(gcd(b%a, a))
gcd(120, 0)
