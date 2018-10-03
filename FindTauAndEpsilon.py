# Medium additional requirement 2 & 3;

from TwistedInt import TwistedInt
from TwistedIntegers import TwistedIntegers
from IteratorOfTwistedIntegers import IteratorOfTwistedIntegers

# Find Tau which Tau(+)x = x;
def FindTau(x,n):
    X = TwistedInt(x,n)
    for ti in IteratorOfTwistedIntegers(TwistedIntegers(n)):
        # Use magic comparison between two TwistedInts;
        if (ti + X == X):
            return ti

# Find Epsilon which Epsilon(*)x = x;
def FindEpsilon(x,n):
    X = TwistedInt(x,n)
    for ti in IteratorOfTwistedIntegers(TwistedIntegers(n)):
        # Use magic comparison between two TwistedInts;
        if (ti * X == X):
            return ti

# Test on FindTau() and FindEpsilon()
# User inputs an integer, print all Tau and Epsilon from <0,input> to <input-1,input>;
def main():
    userInput = int(input("Enter an integer: "))
    print("For n = %i: " % userInput)
    for i in range(userInput):
        print("When x = %s, Tau contains:%s, Epsilon contains: %s;" % (str(i), str(FindTau(i,userInput)),
        str(FindEpsilon(i,userInput))))

if __name__ == "__main__":
    main()
