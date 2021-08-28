import sys

def gcd_euclidean(a,b):
    if a==0:
        return b
    return gcd_euclidean(b%a,a)

def getFactors(n):
    factors = set()
    factors.add(1)
    i = 1
    while i*i < n:
        if n%i==0:
            factors.add(i)
            if n//i!=i:
                factors.add(int(n/i))
        i+=1
    return factors

def commonDivisors(nums):
    gcd = nums[0]
    for i in range(1,len(nums)):
        gcd = gcd_euclidean(gcd,nums[i])
    divisors = getFactors(gcd)
    return divisors
    

def main():
    n = int(sys.argv[1])
    x = 0
    nums = []
    while x<n:
        nums.append(int(sys.argv[x+2]))
        x+=1
    divisors = commonDivisors(nums)
    for x in divisors:
        print(x,end=" ")
    print('')


if __name__ == '__main__':
    main()