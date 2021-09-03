import sys

def extendedEuclidean(a, m):
 
    if a == 0 : 
        return m, 0, 1
            
    gcd, x1, y1 = extendedEuclidean(m%a, a)
    x = y1 - (m//a) * x1
    y = x1
    return gcd, x, y

def main():
    ans = extendedEuclidean(int(sys.argv[1]),int(sys.argv[2]))
    print(ans[1],ans[2],end="")


if __name__ == '__main__':
    main()