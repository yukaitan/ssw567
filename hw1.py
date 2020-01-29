import math
import unittest

def classify_triangle(a, b, c):
    if a+b > c and c+b > a and a+c > b:

        if a == b and b == c and a == c:
            return 'equilateral'
        elif a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
            if a == b or b == c or a == c:
                return 'right and isosceles'
            else:
                return 'right and scalene'
        elif a == b or b == c or a == c:
            return 'isosceles'
        else:
            return 'scalene'
    else:
        return 'not a triangle'
    
        
class Testclassify_triangle(unittest.TestCase):

    def testclassify_triangle(self):
        self.assertEqual('equilateral', classify_triangle(3, 3, 3))
        self.assertEqual('equilateral', classify_triangle(10, 10, 10))
        #self.assertEqual('right and isosceles', classify_triangle(1, 1, math.sqrt(2)))
        self.assertEqual('right and scalene', classify_triangle(3, 4, 5))
        self.assertEqual('right and scalene', classify_triangle(3, 5, 4))
        self.assertEqual('right and scalene', classify_triangle(4, 5, 3))
        self.assertEqual('isosceles', classify_triangle(4, 4, 7))
        self.assertEqual('isosceles', classify_triangle(10, 10, 15))
        self.assertEqual('isosceles', classify_triangle(10, 10, 6))
        self.assertEqual('scalene', classify_triangle(4, 5, 7))
        self.assertEqual('scalene', classify_triangle(5, 7, 8))
        self.assertEqual('not a triangle', classify_triangle(300, 6, 500))
        self.assertEqual('not a triangle', classify_triangle(100, 1, 2))

        

if __name__ == '__main__':
    unittest.main(verbosity=2)

