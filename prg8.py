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
def lcm_(a,b):
    return (a / gcd_euclidean(a,b))* b
    
def checkSol(congruence):
    a= congruence[0]
    b = congruence[1]
    m = congruence[2]
    if b%gcd_euclidean(a,m)==0:
        return True
    else:
        return False

def inverse(a,m):
    if coprimes(a,m):
        _,x,y = extendedEuclidean(a,m)
        inv = (x+m)%m
        return int(inv)

def CRT(congruences):
    # check if all M's are relatively prime
    num1 = congruences[0][2]
    num2 = congruences[1][2]
    lcm = lcm_(num1, num2)
    for i in range(2, len(congruences)):
        lcm = lcm_(lcm, congruences[i][2])
    prod = 1
    for x in congruences:
        prod *=x[2]
    if prod==lcm:
        # all m's are relatively prime
        # now check if all congruences have a solution
        for congruence in congruences:
            if not checkSol(congruence):
                print("Sol does not exist.")
                return
        for congruence in congruences:
            # convert into CRT format
            congruence[1] = (congruence[1]*inverse(congruence[0],congruence[2]))%congruence[2]
            congruence[0] = 1
        M = prod
        ans = 0
        for congruence in congruences:
            b = inverse(M/congruence[2],congruence[2])
            summ = (M/congruence[2])*b*congruence[1]
            ans+=summ
        print(int(ans%M))
    else:
        print("All m's are not relatively prime")


def main():
    n = int(sys.argv[1])
    congruences = []
    for i in range(n):
        a = int(sys.argv[3*i+2])
        b = int(sys.argv[3*i+3])
        m = int(sys.argv[3*i+4])
        congruences.append([a,b,m])
    CRT(congruences)



if __name__ == '__main__':
    main()