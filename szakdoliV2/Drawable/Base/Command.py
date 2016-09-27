# -*- coding: utf-8 -*-

from abc import abstractmethod

from Drawable.Base import AbstractDrawable


class Command(AbstractDrawable):

    @abstractmethod
    def execture_command(self):
        pass;

