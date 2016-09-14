from Rect import Rect
from abc import abstractmethod,ABCMeta


class Command(Rect):
    __metaclass__ = ABCMeta

    def __init__(self, X, Y, H, L, indetLevel):
        super(Rect, self).__init__(X,Y,H,L,indetLevel)
        self.commandName = None

    @abstractmethod
    def runCommand(self):
        pass

    def returnCommandName(self):
        return self.commandName