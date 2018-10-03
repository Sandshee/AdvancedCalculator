# Medium additional requirement 1

from TwistedInt import TwistedInt
from TwistedIntegers import TwistedIntegers

class IteratorOfTwistedIntegers:
    """Iterator for TwistedIntegers"""

    # Constructor
    def __init__(self, twistedInts):
        self.twistedInts = twistedInts
        self.index = -1

    def __iter__(self):
        return self

    # Iteration starts from 0, raises the StopIteration when ends;
    def __next__(self):
        self.index += 1
        if (self.index == self.twistedInts.Size()):
            raise StopIteration
        return self.twistedInts.nList[self.index]
