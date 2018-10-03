from TwistedMatrix import TwistedMatrix

totalPass = True
testFailCount = 0

try:
    print("TEST: Initialize a TwistedMatrix")
    a = TwistedMatrix(2,2)
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None

try:
    print("TEST: Initialize a TwistedMatrix and Assign values to the matrix")
    a = TwistedMatrix(2,2)
    a.AddElement(0,0,0,5)
    a.AddElement(0,1,1,5)
    a.AddElement(1,0,2,5)
    a.AddElement(1,1,3,5)
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None

try:
    print("TEST: Check the value assigned to matrices is correct")
    a = TwistedMatrix(2,2)
    a.AddElement(0,0,0,5)
    a.AddElement(0,1,1,5)
    a.AddElement(1,0,2,5)
    a.AddElement(1,1,3,5)
    b = TwistedMatrix(2,2)
    b.AddElement(0,0,0,5)
    b.AddElement(0,1,1,5)
    b.AddElement(1,0,2,5)
    b.AddElement(1,1,3,5)

    for i in range(0,2):
        for j in range(0,2):
            if(a.matrix[i][j] != b.matrix[i][j]):
                print("failed")
                totalPass = False
                testFailCount += 1
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None

try:
    print("TEST: Check normal matrices addition")
    a = TwistedMatrix(2,2)
    a.AddElement(0,0,0,5)
    a.AddElement(0,1,1,5)
    a.AddElement(1,0,2,5)
    a.AddElement(1,1,3,5)
    b = TwistedMatrix(2,2)
    b.AddElement(0,0,1,5)
    b.AddElement(0,1,2,5)
    b.AddElement(1,0,3,5)
    b.AddElement(1,1,4,5)
    c = a + b

    # [0,1] + [1,2] = [1,3]
    # [2,3]   [3,4]   [0,2]
    result = TwistedMatrix(2,2)
    result.AddElement(0,0,1,5)
    result.AddElement(0,1,3,5)
    result.AddElement(1,0,0,5)
    result.AddElement(1,1,2,5)

    for i in range(0,2):
        for j in range(0,2):
            if(c.matrix[i][j] != result.matrix[i][j]):
                print("failed")
                totalPass = False
                testFailCount += 1
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None
result = None

try:
    print("TEST: Check matrices addition with 'None's")
    a = TwistedMatrix(2,2)
    a.AddElement(0,0,0,5)
    a.AddElement(1,0,2,5)
    a.AddElement(1,1,3,5)
    b = TwistedMatrix(2,2)
    b.AddElement(0,0,1,5)
    b.AddElement(0,1,2,5)
    b.AddElement(1,1,4,5)
    c = a + b

    # [0,None] + [1,2   ] = [1,Undefined]
    # [2,3   ]   [None,4]   [Undefined,2]
    result = TwistedMatrix(2,2)
    result.AddElement(0,0,1,5)
    result.matrix[0][1] = "Undefined"
    result.matrix[1][0] = "Undefined"
    result.AddElement(1,1,2,5)

    for i in range(0,2):
        for j in range(0,2):
            if(c.matrix[i][j] != result.matrix[i][j]):
                print("failed")
                totalPass = False
                testFailCount += 1
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None
result = None

try:
    print("TEST: Check matrices addition which elements with different n")
    a = TwistedMatrix(2,2)
    a.AddElement(0,0,0,7)
    a.AddElement(0,1,1,5)
    a.AddElement(1,0,2,5)
    a.AddElement(1,1,3,4)
    b = TwistedMatrix(2,2)
    b.AddElement(0,0,1,5)
    b.AddElement(0,1,2,5)
    b.AddElement(1,0,3,5)
    b.AddElement(1,1,4,5)
    c = a + b

    # [0*,1] + [1,2] = [Undefined,3]
    # [2,3*]   [3,4]   [0,Undefined]
    result = TwistedMatrix(2,2)
    result.matrix[0][0] = "Undefined"
    result.AddElement(0,1,3,5)
    result.AddElement(1,0,0,5)
    result.matrix[1][1] = "Undefined"

    for i in range(0,2):
        for j in range(0,2):
            if(c.matrix[i][j] != result.matrix[i][j]):
                print("failed")
                totalPass = False
                testFailCount += 1
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None
result = None

try:
    print("TEST: Check normal matrices multiplication")
    a = TwistedMatrix(2,3)
    a.AddElement(0,0,0,5)
    a.AddElement(0,1,1,5)
    a.AddElement(0,2,2,5)
    a.AddElement(1,0,3,5)
    a.AddElement(1,1,4,5)
    a.AddElement(1,2,0,5)
    b = TwistedMatrix(3,2)
    b.AddElement(0,0,0,5)
    b.AddElement(0,1,1,5)
    b.AddElement(1,0,2,5)
    b.AddElement(1,1,3,5)
    b.AddElement(2,0,4,5)
    b.AddElement(2,1,0,5)
    c = a * b

    # [0,1,2] * [0,1] = [4,0]
    # [3,4,0]   [2,3]   [1,1]
    #           [4,0]
    result = TwistedMatrix(2,2)
    result.AddElement(0,0,4,5)
    result.AddElement(0,1,0,5)
    result.AddElement(1,0,1,5)
    result.AddElement(1,1,1,5)

    for i in range(0,2):
        for j in range(0,2):
            if(c.matrix[i][j] != result.matrix[i][j]):
                print("failed")
                totalPass = False
                testFailCount += 1
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None
result = None

try:
    print("TEST: Check matrices multiplication with 'None's")
    a = TwistedMatrix(2,3)
    a.AddElement(0,0,0,5)
    a.AddElement(0,1,1,5)
    a.AddElement(0,2,2,5)
    a.AddElement(1,0,3,5)
    a.AddElement(1,1,4,5)
    b = TwistedMatrix(3,2)
    b.AddElement(0,0,0,5)
    b.AddElement(0,1,1,5)
    b.AddElement(1,0,2,5)
    b.AddElement(1,1,3,5)
    b.AddElement(2,0,4,5)
    c = a * b

    # [0,1,2   ] * [0,1    ] = [4,Undefined        ]
    # [3,4,None]   [2,3   ]    [Undefined,Undefined]
    #              [4,None]
    result = TwistedMatrix(2,2)
    result.AddElement(0,0,4,5)
    result.matrix[0][1] = "Undefined"
    result.matrix[1][0] = "Undefined"
    result.matrix[1][1] = "Undefined"

    for i in range(0,2):
        for j in range(0,2):
            if(c.matrix[i][j] != result.matrix[i][j]):
                print("failed")
                totalPass = False
                testFailCount += 1
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None
result = None

try:
    print("TEST: Check matrices multiplication which elements with different n")
    a = TwistedMatrix(2,3)
    a.AddElement(0,0,0,1)
    a.AddElement(0,1,1,5)
    a.AddElement(0,2,2,5)
    a.AddElement(1,0,3,5)
    a.AddElement(1,1,4,5)
    a.AddElement(1,2,0,5)
    b = TwistedMatrix(3,2)
    b.AddElement(0,0,0,5)
    b.AddElement(0,1,1,5)
    b.AddElement(1,0,2,5)
    b.AddElement(1,1,3,5)
    b.AddElement(2,0,4,5)
    b.AddElement(2,1,0,5)
    c = a * b

    # [0*,1,2] * [0,1] = [Undefined,Undefined]
    # [3,4,0 ]   [2,3]   [1,1                ]
    #            [4,0]
    result = TwistedMatrix(2,2)
    result.matrix[0][0] = "Undefined"
    result.matrix[0][1] = "Undefined"
    result.AddElement(1,0,1,5)
    result.AddElement(1,1,1,5)

    for i in range(0,2):
        for j in range(0,2):
            if(c.matrix[i][j] != result.matrix[i][j]):
                print("failed")
                totalPass = False
                testFailCount += 1
    print("passed")
except:
    print("failed")
    totalPass = False
    testFailCount += 1

a = None
b = None
c = None
result = None

if(totalPass):
    print("\nAll TwistedInt tests passed.")
elif(testFailCount == 1):
    print("\n1 test has failed.")
else:
    print("\n%s tests have failed." % (testFailCount))
