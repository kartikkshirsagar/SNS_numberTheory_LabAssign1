import sys
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

def phi(n):
    p=2     
    result=n
    while p * p <= n:
        if (n % p == 0):
            while n % p == 0:
                n = int(n / p)
            result = result - int(result / p)
        p = p+1
    if n > 1:
        result -= int(result / n)
    return result

def calcExp(a,x,n):
    temp = x
    if checkPrime(n):
        totient = n-1
        x = x%totient
        # print("{4}^{0}( mod {1} ) ≡ {4}^{2}( mod {1} ) * {4}^({5} * {3})(mod {1})".format(temp,n,x,temp//totient,a,totient))
        # print("{0}^{1}( mod {2} ) ≡ {0}^{3}( mod {2} ) * 1".format(a,temp,n,x))
        return (a**x)%n
    else:
        totient = phi(n)
        x = x%totient
        # print("{4}^{0}( mod {1} ) ≡ {4}^{2}( mod {1} ) * {4}^({5} * {3})(mod {1})".format(temp,n,x,temp//totient,a,totient))
        # print("{0}^{1}( mod {2} ) ≡ {0}^{3}( mod {2} ) * 1".format(a,temp,n,x))
        return (a**x)%n



def main():
    a = int(sys.argv[1])
    x = int(sys.argv[2])
    n = int(sys.argv[3])
    
    ans = calcExp(a,x,n)
    print(int(ans),end="")



if __name__ == '__main__':
    main()