import sys
import math

def coprimes(a,b):
    if gcd_euclidean(a,b)==1:
        return True
    else:
        return False

def phi(m):
    if checkPrime(m):
        return m-1
    ct=0
    for i in range(1,m):
        if coprimes(i,m):
            ct+=1
    return ct

def getDivisors(n):
    i = 1
    divisors = []
    while i*i<=n:
        if n%i==0:
            divisors.append(i)
            if n/i!=i:
                divisors.append(n//i)
        i+=1
    return divisors

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

def orderUnderModulo(a,m):
    if gcd_euclidean(a,m)==1:
        totient = phi(m)
        divisors = sorted(getDivisors(totient))
        for divisor in divisors:
            if math.pow(a,divisor)%m==1:
                return divisor
        return totient


def main():
    a = int(sys.argv[1])
    m = int(sys.argv[2])
    ans = orderUnderModulo(a,m)
    print(int(ans))
    



if __name__ == '__main__':
    main()