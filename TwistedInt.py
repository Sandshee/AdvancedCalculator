# Basic requirement

import math

class TwistedInt:
    """TwistedInt class"""

    # Constructor
    # Negative values of val and n are allowed (e.g. <-1,5>, <2,-4>), but absolute
    #   value of 'val' must be greater than absolute value of 'n' (e.g. <6,5> or
    #   <-3,-1> is now allowed);
    def __init__(self, val, n):
        if (abs(val) >= abs(n)):
            raise Exception ("Invalid value")
        else:
            self.value = val
            self.n = n

    # Overwrite print() method;
    # (a,n) is printed as "<a,n>";
    def __str__(self):
        return "<" + str (self.value) + ":" + str (self.n) + ">"

    # Re-define "==" for two TwistedInts' comparison;
    def __eq__ (self, other):
        if(type(other) != TwistedInt):
            return False
        else:
            return ((self.value == other.value) and (self.n == other.n))

    # Re-define "+" for two TwistedInts' addition;
    # (a,n)(+)(b,n) = (a+b) mod n;
    def __add__(self, other):
        if (self.n == other.n):
            if (isinstance(self.value, complex) or isinstance(self.n, complex) or isinstance(other.value, complex)):
                return TwistedInt (TwistedInt.complexModulo((self.value + other.value),self.n), self.n)
            else:
                return TwistedInt ((self.value + other.value) % self.n, self.n)
        else:
            raise Exception("Invalid add operation")

    # Re-define "*" for two TwistedInts' multiplication;
    # (a,n)(*)(b,n) = (a+b+a*b) mod n;
    def __mul__ (self, other):
        if (self.n == other.n):
            if (isinstance(self.value, complex) or isinstance(self.n, complex) or isinstance(other.value, complex)):
                return TwistedInt (TwistedInt.complexModulo((self.value + other.value + self.value * other.value), self.n)
                , self.n)
            else:
                return TwistedInt ((self.value + other.value + self.value * other.value) % self.n
                , self.n)
        else:
            raise Exception("Invalid multiply operation")

    # Defines a new method, complexCeiling which calculates the ceiling of a complex number.
    def complexCeiling (number):
        return complex(math.ceil(number.real),round(math.ceil(number.imag)))

    # Defines a new method, complexModulo which calculates the modulo (at least an approximation) of two complex numbers.
    def complexModulo (a,b):
        q = a/b

        qr = round(q.real)
        qi = round(q.imag)

        r = a.real + (b.imag * qi) - (b.real * qr)
        i = a.imag - (b.real * qi) - (b.imag * qr)

        #The previous modulo of Complex Numbers, one of the basic ones found by Wolfram Alpha
        #return a + b*TwistedInt.complexCeiling(-(a/b))
        return complex(r, i)
