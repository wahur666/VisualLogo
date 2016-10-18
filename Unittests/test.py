import unittest

from System.Vector2 import Vector2
from System.SupportFunctions import MoveListElement

class TestVectorMethods(unittest.TestCase):

    def test_Lerp(self):
        v1 = Vector2(0,0)
        v2 = Vector2(2,2)

        self.assertEqual( Vector2.Lerp(v1, v2, 0.5), Vector2(1,1))
        self.assertEqual(Vector2.Lerp(v1, v2, 1), Vector2(2, 2))
        self.assertEqual(Vector2.Lerp(v1, v2, 0), Vector2(0, 0))

    def test_eq(self):
        v1 = Vector2(0,0)
        v2 = Vector2(0,0)
        self.assertEqual(v1, v2)

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