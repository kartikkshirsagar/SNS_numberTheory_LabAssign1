import sys

def extendedEuclidean(a,b):
    # input -> two non-negative integers a and b
    # output -> (d,x,y) where d=gcd(a,b) and x,y such that ax+by = d
    if b>a:
        # a >=b necessary
        a,b=b,a
    if b==0:
        gcd=a
        x=1
        y=0
        return (gcd,x,y)
    x1 = 0
    x2 = 1
    y1 = 1
    y2 = 0
    while b>0:
        quotient = a//b
        remainder = a-quotient*b
        x = x2 - quotient*x1
        y = y2 - quotient*y1
        a = b
        b = remainder
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    gcd = a
    x = x2
    y = y2
    return (gcd,x,y)

def gcd_euclidean(a,b):
    if a==0:
        return b
    return gcd_euclidean(b%a,a)

def coprimes(a,b):
    if gcd_euclidean(a,b)==1:
        return True
    else:
        return False

def inverse(a,m):
    if coprimes(a,m):
        _,x,y = extendedEuclidean(a,m)
        inv = (y+m)%m
        return inv
    else:
        return 1

def solveCongruence(a,b,m):
    gcd = gcd_euclidean(a,m)
    if b%gcd==0:
        print("Y",end=' ')
        print(gcd,end=' ')
        # x = beta*alphainv mod U
        beta = b/gcd
        alpha = a/gcd
        U = m/gcd
        alphainv = inverse(alpha,U)
        ans = (beta*alphainv)%U
        i=0
        while i<gcd:
            print(int(ans+i*U),end=' ')
            i+=1 
        print('')
    else:
        print("N")
def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    m = int(sys.argv[3])
    solveCongruence(a,b,m)
    



if __name__ == '__main__':
    main()