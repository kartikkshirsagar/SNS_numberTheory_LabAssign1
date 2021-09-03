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
        print("Y",end = ' ')
        _,x,y = extendedEuclidean(a,m)
        inv = (x+m)%m
        print(int(inv),end="")
    else:
        print("N",end="")

def main():
    a = int(sys.argv[1])
    m = int(sys.argv[2])
    inverse(a,m)
    



if __name__ == '__main__':
    main()