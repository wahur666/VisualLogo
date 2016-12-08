import unittest

from System.SupportFunctions import MoveListElement


class TestSupportFunctions(unittest.TestCase):

    def test_MoveListElement(self):

        a1 = [1,2,3,4,5,6]
        a2 = [1,2,3,4,5,6]
        a3 = [1,2,3,4,5,6]
        a4 = [1,2,3,4,5,6]

        self.assertEquals(MoveListElement(a1, 3, 0), [3,1,2,4,5,6])
        self.assertEquals(MoveListElement(a2, 6, 2), [1,2,6,3,4,5])
        self.assertEquals(MoveListElement(a3, 1, 5), [2,3,4,5,6,1])
        self.assertEquals(MoveListElement(a4, 2, 1), [1,2,3,4,5,6])