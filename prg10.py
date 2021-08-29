import math
import sys
#euclid algo for gcd calculation

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

def phi(m):
    if checkPrime(m):
        return m-1
    ct=0
    for i in range(1,m):
        if coprimes(i,m):
            ct+=1
    return ct

def gcd_euclidean(a,b):
    if a==0:
        return b
    return gcd_euclidean(b%a,a)

#get prime factos of m
def get_prime_factors(m):

    s = set()

    for i in range(2, int(math.sqrt(m))+1):
         
        while (m % i == 0) :
 
            s.add(i)
            m = m // i

    if (m > 2) :
        s.add(m)

    return list(s)

def coprimes(a,b):
    if gcd_euclidean(a,b)==1:
        return True
    else:
        return False

#get reduced residue modulo set
def getRRSM(m):
    RRSM = []
    for i in range(1,m):
        if coprimes(i,m):
            RRSM.append(i)
    return RRSM








def main():
    #get  and m
    m = int(sys.argv[1])
    primitiveRoots(m)

def primitiveRoots(m):
    phi_ = phi(m)
    num_roots = phi(phi_)
    divisors = get_prime_factors(phi_)
    rrsm_set = getRRSM(m)

    print(num_roots, end=" ")

    for ele in rrsm_set:

        flag = True

        for div in divisors:

            if (ele**(phi_//div))%m == 1:
                flag = False
        
        if flag:
            print(ele, end=" ")
    print('')


if __name__ == '__main__':
    main()