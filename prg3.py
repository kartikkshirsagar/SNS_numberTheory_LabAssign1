import sys

def primeFactors(n):
    i = 3
    pFactors = []
    while n%2==0:
        pFactors.append(2)
        n=n//2
    while i*i<=n:
        while n%i==0:
            pFactors.append(i)
            n=n//i        
        i+=2
    if n>2:
        pFactors.append(n)

    return pFactors

def main():
    n = int(sys.argv[1])
    pFactors = primeFactors(n)
    print(pFactors)
if __name__ == '__main__':
    main()