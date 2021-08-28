import sys
import math
def checkPrime(n):
    if n==2:
        return True
    if n%2==0 or n==1 or n==0:
        return False
    i = 3
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
    return True

def gcd_euclidean(a,b):
    if a==0:
        return b
    return gcd_euclidean(b%a,a)

def coprimes(a,b):
    if gcd_euclidean(a,b)==1:
        return True
    else:
        return False

def phi(m):
    ct=0
    for i in range(1,m):
        if coprimes(i,m):
            ct+=1
    return ct

def calcExp(a,x,n):
    temp = x
    if checkPrime(n):
        totient = n-1
        x = x%totient
        print("{4}^{0}( mod {1} ) ≡ {4}^{2}( mod {1} ) * {4}^({5} * {3})(mod {1})".format(temp,n,x,temp//totient,a,totient))
        print("{0}^{1}( mod {2} ) ≡ {0}^{3}( mod {2} ) * 1".format(a,temp,n,x))
        return math.pow(a,x)%n
    else:
        totient = phi(n)
        x = x%totient
        print("{4}^{0}( mod {1} ) ≡ {4}^{2}( mod {1} ) * {4}^({5} * {3})(mod {1})".format(temp,n,x,temp//totient,a,totient))
        print("{0}^{1}( mod {2} ) ≡ {0}^{3}( mod {2} ) * 1".format(a,temp,n,x))
        return math.pow(a,x)%n



def main():
    a = int(sys.argv[1])
    x = int(sys.argv[2])
    n = int(sys.argv[3])
    
    ans = calcExp(a,x,n)
    print("= ",int(ans))



if __name__ == '__main__':
    main()