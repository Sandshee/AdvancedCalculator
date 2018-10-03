# Easy additional requirement 3

from TwistedInt import TwistedInt

class TwistedIntegers:
    """TwistedIntegers class"""

    # Constructor
    # Each instance will store a list of TwistedInts from <0,n> to <n-1,n> (positive)
    #   or <n+1,n> (negative);
    def __init__(self, n):
        self.nList = []
        if(n >= 0):
            for i in range(0, n):
                self.nList.append(TwistedInt(i,n))
        else:
            for i in range(n+1, 1):
                self.nList.append(TwistedInt(i,n))

    # Overwrite print() method;
    def __str__(self):
        self.listStr = "["
        for ints in self.nList:
            self.listStr += str(ints)
        self.listStr += "]"
        return self.listStr

    # Return the size of list;
    def Size(self):
        return len(self.nList)
