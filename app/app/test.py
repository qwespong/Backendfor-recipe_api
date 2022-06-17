"""
Sample tests
"""

from django.test import SimpleTestCase

from app import Calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    
    def test_add_numbers(self):
        """Test adding numbers together"""
        res = Calc.add(5,6)
        
        self.assertEqual(res, 11)


    def test_sub_numbers(self):
        """Subtract two numbers"""
        res = Calc.sub(10,15)

        self.assertEqual(res, 5)