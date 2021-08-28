import sys

def gcd_euclidean(a,b):
    if a==0:
        return b
    return gcd_euclidean(b%a,a)

def coprimes(a,b):
    if gcd_euclidean(a,b)==1:
        return True
    else:
        return False

def getRRSM(m):
    RRSM = []
    for i in range(1,m):
        if coprimes(i,m):
            RRSM.append(i)
    return RRSM

def main():
    m = int(sys.argv[1])
    RRSM = getRRSM(m)
    print(RRSM," phi(m) = ",len(RRSM))




if __name__ == '__main__':
    main()