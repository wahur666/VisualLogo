# -*- coding: utf-8 -*-
from math import sqrt

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod                       #Percent [0-1]
    def Lerp(first_vector, second_vector, t):
        return Vector2(first_vector.x*(1-t) + second_vector.x*t, first_vector.y*(1-t) + second_vector.y*t)

    @staticmethod
    def Distance(first_vector, second_vector):
        return sqrt((first_vector.x-second_vector.x)**2 + (first_vector.y-second_vector.y)**2)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__dict__ == other.__dict__
        else:
            return False
