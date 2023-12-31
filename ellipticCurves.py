class Point:

    # y^2 = x^3 + ax + b
    # y^2 = x^3 + 5x + 7
    # sepc256k1 -> y^2 = x^3 + 7 (a = 0, b = 7)
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) are not ion the curve'.format(x, y))
        
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b
    

    def __ne__(self, other):
        return not (self == other)
    

    def __add__(self, other):

        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {} and {} are not on the same curve'.format(self, other))

        if self.x is None:
            return other
        if other.x is None:
            return self
        
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)
        

# check if on a curve where a == 5 and b == 7
def onCurve(x, y):
    return y**2 == x**3 + 5*x + 7


def onSepc256k1(x, y):
    return y**2 == x**3 + 7