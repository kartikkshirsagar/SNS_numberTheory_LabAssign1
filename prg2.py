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

def main():
    ans = extendedEuclidean(int(sys.argv[1]),int(sys.argv[2]))
    print(ans)


if __name__ == '__main__':
    main()