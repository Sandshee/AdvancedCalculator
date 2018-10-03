# Easy additional requirement 2

from TwistedInt import TwistedInt

# x(+)y = y(+)x
def rule1(x,y):
    return (x + y == y + x)

# x(*)y = y(*)x
def rule2(x,y):
    return (x * y == y * x)

# (x(+)y)(+)z = x(+)(y(+)z)
def rule3(x,y,z):
    return ((x + y) + z == x + (y + z))

# (x(*)y)(*)z = x(*)(y(*)z)
def rule4(x,y,z):
    return ((x * y) * z == x * (y * z))

# (x(+)y)(*)z = (x(*)z)(+)(y(*)z)
def rule5(x,y,z):
    return ((x + y) * z == (x * z) + (y * z))

def convertDown(n):
    if(isinstance(n,complex)):
        if(n.imag == 0):
            n = n.real
            if(n//1 == n):
                n = int(n)

    return n

# Test for rule1() to rule5()
# User inputs 4 integers to form 3 TwistedInts of x, y and z, print the result of
#   testing 5 rules;
def main():
    n = convertDown(complex(input("Enter an integer for n: ")))
    xInp = convertDown(complex(input("Enter an integer for x: ")))
    yInp = convertDown(complex(input("Enter an integer for y: ")))
    zInp = convertDown(complex(input("Enter an integer for z: ")))

    if(abs(xInp) >= abs(n) or abs(yInp) >= abs(n) or abs(zInp) >= abs(n)):
        print("Invalid x/y/z")
    else:

        X = TwistedInt(xInp,n)
        Y = TwistedInt(yInp,n)
        Z = TwistedInt(zInp,n)

        print("When x = %s, y = %s, z = %s: " % (str(X), str(Y), str(Z)))
        print("x + y = y + x is:", rule1(X,Y))
        print("x * y = y * x is:", rule2(X,Y))
        print("(x + y) + z = x + (y + z) is:", rule3(X,Y,Z))
        print("(x * y) * z = x * (y * z)) is:", rule4(X,Y,Z))
        print("(x + y) * z = (x * z) + (y * z)) is:", rule5(X,Y,Z))

if __name__ == "__main__":
    main()
