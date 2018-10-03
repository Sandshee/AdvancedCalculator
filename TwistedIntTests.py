from TwistedInt import TwistedInt

#A switch, only flipped upon a failed test
totalPass = True

#Counts how many tests actually fail
testFailCount = 0

#A whole series of tests: if a single test fails, totalPass is set to false, then the test begins counting the failed cases
#After each test, every variable is set to 0 to avoid any complications
#Some tests involve expected exceptions, so the passed and failed statements are switched around.
#Only tests which failed at one point have expected outputs printed, this is to save time as it seems un-necissary until the test actually fails.

try:
    print("TEST: Assigning Values to TwistedInt")
    a = TwistedInt(3,5)
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None

try:
    print("TEST: Re-assigning Values to TwistedInt")
    a = TwistedInt(3,5)
    a = TwistedInt(6,9)
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None

try:
    print("TEST: Checking with val > n")
    a = TwistedInt(6,2)
    print("failed")
    totalPass = False
    testFailCount += 1
except:
    print("passed")

a = None

try:
    print("TEST: Checking equals")
    a = TwistedInt(6,9)
    b = TwistedInt(6,9)

    if(a == b):
        print("passed")
    else:
        print("failed")
        totalPass = False
        testFailCount += 1
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None

try:
    print("TEST: Testing addition with known values")
    a = TwistedInt(2,5)
    b = TwistedInt(4,5)

    if(a+b == TwistedInt(1,5)):
        print("passed")
    else:
        print("failed")
        totalPass = False
        testFailCount += 1
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None

try:
    print("TEST: Testing multiplication with known values")
    a = TwistedInt(2,5)
    b = TwistedInt(4,5)

    if(a*b == TwistedInt(4,5)):
        print("passed")
    else:
        print("failed")
        totalPass = False
        testFailCount += 1
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None

try:
    print("TEST: Checking use of floating point numbers")
    a = TwistedInt(3.5,3.9)
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None

try:
    print("TEST: Testing addition with known floating point numbers")
    a = TwistedInt(2.9,5.3)
    b = TwistedInt(4.2,5.3)
    c = TwistedInt(round((a+b).value,4),(a+b).n)

    if(c == TwistedInt(1.8,5.3)):
        print("passed")
    else:
        print("failed: expected <1.8,5.3>, actual value: %s" % (c))
        totalPass = False
        testFailCount += 1
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None

try:
    print("TEST: Testing multiplication with known floating point numbers")
    a = TwistedInt(2.9,5.3)
    b = TwistedInt(4.2,5.3)
    c = TwistedInt(round((a*b).value,5),(a*b).n)

    if(c == TwistedInt(3.38,5.3)):
        print("passed")
    else:
        print("failed: expected <3.38,5.3>, actual value: %s" % (c))
        totalPass = False
        testFailCount += 1
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None

try:
    print("TEST: Testing addition with floats and ints")
    a = TwistedInt(2.9,5.3)
    b = TwistedInt(4,5.3)
    c = TwistedInt(round((a+b).value,4),(a+b).n)

    if(c == TwistedInt(1.6,5.3)):
        print("passed")
    else:
        print("failed: expected <1.6,5.3>, actual value: %s" % (c))
        totalPass = False
        testFailCount += 1
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None

try:
    print("TEST: Testing multiplication with floats and ints")
    a = TwistedInt(2.9,5.3)
    b = TwistedInt(4,5.3)
    c = TwistedInt(round((a*b).value,4),(a*b).n)

    if(c == TwistedInt(2.6,5.3)):
        print("passed")
    else:
        print("failed: expected <2.6,5.3>, actual value: %s" % (c))
        totalPass = False
        testFailCount += 1
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None

try:
    print("TEST: Checking use of negative numbers")
    a = TwistedInt(-4,-9)
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None

try:
    print("TEST: Checking abs of negative numbers")
    a = TwistedInt(-9,-2)
    print("failed")
    totalPass = False
    testFailCount += 1
except:
    print("passed")

a = None

try:
    print("TEST: Checking abs of negative and positive numbers, expected exception")
    a = TwistedInt(-9,2)
    print("failed")
    totalPass = False
    testFailCount += 1
except:
    print("passed")

a = None

try:
    print("TEST: Checking abs of negative and positive numbers, expected nothing")
    a = TwistedInt(2,-4)
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None

try:
    print("TEST: Testing addition with negative numbers")
    a = TwistedInt(2,3)
    b = TwistedInt(-1,3)

    if(a+b == TwistedInt(1,3)):
        print("passed")
    else:
        print("failed")
        totalPass = False
        testFailCount += 1
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None

try:
    print("TEST: Testing multiplication with negative numbers")
    a = TwistedInt(2,3)
    b = TwistedInt(-1,3)

    if(a*b == TwistedInt(2,3)):
        print("passed")
    else:
        print("failed, expected value <2,3>, actual value %s" % (a*b))
        totalPass = False
        testFailCount += 1
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None

try:
    print("TEST: Checking use of complex numbers")
    a = TwistedInt(2+2j,4+4j)
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None

try:
    print("TEST: Checking abs of complex numbers")
    a = TwistedInt(2+2j,1+1j)
    print("failed")
    totalPass = False
    testFailCount += 1
except:
    print("passed")

a = None

try:
    print("TEST: Checking use of complex numbers and integers, expected exception")
    a = TwistedInt(2+2j,2)
    print("failed")
    totalPass = False
    testFailCount += 1
except:
    print("passed")

a = None

try:
    print("TEST: Checking use of complex numbers and integers, expected nothing")
    a = TwistedInt(2+2j,3)
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None

try:
    print("TEST: Testing addition of complex numbers")
    a = TwistedInt(2+2j,3)
    b = TwistedInt(1+2j,3)
    if (a+b == TwistedInt(1j,3)):
        print("passed")
    else:
        print("fail, expected value: <1j,3>, actual value %s" % (a+b))
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None

a = None

try:
    print("TEST: Testing multiplication of complex numbers")
    a = TwistedInt(2+2j,3)
    b = TwistedInt(1+2j,3)
    if (a*b == TwistedInt(1+1j,3)):
        print("passed")
    else:
        print("fail, expected value: <1+1j,3>, actual value %s" % (a*b))
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None


if(totalPass):
    print("\nAll TwistedInt tests passed.")
elif(testFailCount == 1):
    print("\n1 test has failed.")
else:
    print("\n%s tests have failed." % (testFailCount))
