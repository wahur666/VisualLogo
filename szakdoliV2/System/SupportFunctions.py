# -*- coding: utf-8 -*-

def MoveListElement(list , element, index):
    # type: (list, object, int)
    list.remove(element)
    list.insert(index, element)
    return  list
