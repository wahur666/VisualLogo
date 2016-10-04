import unittest

from System.Vector2 import Vector2

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