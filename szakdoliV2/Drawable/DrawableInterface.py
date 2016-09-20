from abc import ABCMeta, abstractmethod


class DrawableInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def DrawObject(self, screen):
        pass

    @abstractmethod
    def IsInside(self, position):
        pass