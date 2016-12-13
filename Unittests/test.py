import unittest

from System.SupportFunctions import MoveListElement, SplitCommand
from Drawable.LogoModule.Turtle import Turtle


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

    def test_SplitCommand(self):
        self.assertSequenceEqual(SplitCommand("<class=Loop, loop_index=2, cycle_number=8>"), {"class" : "Loop", "loop_index" : "2", "cycle_number" : "8"})
        self.assertSequenceEqual(SplitCommand("<class=Right, mul=3>"), {"class" : "Right", "mul" : "3"})
        self.assertSequenceEqual(SplitCommand("<class=Forward, mul=2>"), {"class" : "Forward", "mul" : "2"})
        self.assertSequenceEqual(SplitCommand("<class=LoopEnd, loop_index=2>"), {"class" : "LoopEnd", "loop_index" : "2"})
        self.assertSequenceEqual(SplitCommand("<class=PenUp>"), {"class" : "PenUp"})
        self.assertIsNone(SplitCommand("< class=PenUp >"))




class TestTurtle(unittest.TestCase):

    def test_Turtle(self):
        # Inicializacio
        turtle = Turtle()
        (x, y), rot, show = turtle.GetTurtleInformationToRender()

        # Elore
        turtle.forward()
        self.assertSequenceEqual(turtle.GetTurtleInformationToRender(), ((x + 20, y), rot, show))

        # Hatra
        turtle.backward()
        self.assertSequenceEqual(turtle.GetTurtleInformationToRender(), ((x, y), rot, show))

        # Balra
        turtle.left()
        self.assertSequenceEqual(turtle.GetTurtleInformationToRender(), ((x, y), (rot - 90) % 360, show))

        # Jobbra
        turtle.right()
        self.assertSequenceEqual(turtle.GetTurtleInformationToRender(), ((x, y), (rot) % 360, show))

        # Home
        turtle.forward()
        turtle.forward()
        turtle.home()
        self.assertSequenceEqual(turtle.GetTurtleInformationToRender(), ((x, y), rot, show))

        # HideTurtle
        turtle.hideturtle()
        self.assertSequenceEqual(turtle.GetTurtleInformationToRender(), ((x, y), rot, False))

        # ShowTurtle
        turtle.showturtle()
        self.assertSequenceEqual(turtle.GetTurtleInformationToRender(), ((x, y), rot, True))

