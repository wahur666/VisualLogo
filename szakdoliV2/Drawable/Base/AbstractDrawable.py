# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractDrawable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def DrawObject(self, screen):
        pass

    @abstractmethod
    def IsInside(self, position):
        pass