import sys

def extendedEuclidean(a, m):
 
    if a == 0 : 
        return m, 0, 1
            
    gcd, x1, y1 = extendedEuclidean(m%a, a)
    x = y1 - (m//a) * x1
    y = x1
    return gcd, x, y

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
        inv = (x+m)%m
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