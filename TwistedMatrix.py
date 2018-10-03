# Hard additional requirement 1

from TwistedInt import TwistedInt

class TwistedMatrix:
    """TwistedMatrix class"""

    # Constructor
    # The 2-D array is initialized with 'None's, user should add new TwistedInts by
    #   AddElement() method;
    def __init__(self, row, col):
        self.matrix = [[None for x in range(col)] for y in range(row)]
        self.row = row
        self.col = col

    # Overwrite print() method;
    def __str__(self):
        for i in range(self.row):
            print("[ ", end = "")
            for j in range(self.col):
                print(self.matrix[i][j], end = " ")
            print("]")
        return "A %s*%s TwistedInt matrix" % (str(self.row), str(self.col))

    # Add a new TwistedInt of <val,n> into the matrix at 'row' row & 'col' col;
    def AddElement(self, row, col, val, n):
        if(row >= self.row or col >= self.col):
            raise Exception("Out of matrix bound")
        else:
            ti = TwistedInt(val,n)
            self.matrix[row][col] = ti

    # TwistedMatrix addition;
    # Result is either a 'undefined'(TwistedInts with different n are added together
    #   or one of the factor is 'None') or the sum of two TwistedInts;
    def __add__(self, other):
        if(self.row != other.row or self.col != other.col):
            raise Exception("Matrices with different size cannot be added together")
        else:
            result = TwistedMatrix(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    if(self.matrix[i][j] == None or other.matrix[i][j] == None or
                    self.matrix[i][j].n != other.matrix[i][j].n):
                        result.matrix[i][j] = "Undefined"
                    else:
                        result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result

    # TwistedMatrix multiplicaiton;
    # Assume self * other, self.col should equals to other.row, the multiplication
    #   follows 'Row-by-Column' rule, result is either a 'undefined' (TwistedInts
    #   with different n are added/multiplied together or one of the factor is 'None')
    #   or the product of 'Row-by-Column' rule;
    def __mul__(self, other):
        if(self.col != other.row):
            raise Exception("Row-by-Column rule cannot be applied")
        else:
            result = TwistedMatrix(self.row, other.col)
            for i in range(self.row):
                for j in range(other.col):
                    for k in range(self.col):
                        if(self.matrix[i][k] == None or other.matrix[k][j] == None
                        or self.matrix[i][k].n != other.matrix[k][j].n):
                            result.matrix[i][j] = "Undefined"
                        else:
                            temp = self.matrix[i][k] * other.matrix[k][j]
                            if(result.matrix[i][j] == None):
                                result.matrix[i][j] = temp
                            elif(result.matrix[i][j] == "Undefined"):
                                result.matrix[i][j] = "Undefined"
                            else:
                                result.matrix[i][j] += temp
            return result
