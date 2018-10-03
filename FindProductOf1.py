# Easy additional requirement 1

from TwistedInt import TwistedInt

# Find x which x(*)x = 1;
def FindProductOf1(n):
    result = TwistedInt(1,n)
    for i in range (1,n):
        X = TwistedInt(i,n)
        if(X * X == result):
            return X

# Test on FindProductOf1()
# User inputs two integers bound for n, print all <x,n> that satisfies x * x = 1;
def main():
    lowerBound = int(input("Enter the lower bound of n(at least 2): "))
    upperBound = int(input("Enter the upper bound of n: "))
    if(upperBound <= lowerBound or lowerBound < 2):
        print("Invalid bounds")
    else:
        for i in range(lowerBound,upperBound+1):
            print("When n = %s, x that satisfies x * x = <1,%s> are:%s"
            % (str(i), str(i), str(FindProductOf1(i))))

if __name__ == "__main__":
    main()
