# -*- coding: utf-8 -*-
from Drawable.LogoModule.DrawableCommands import *
from Vector2 import Vector2

import sys
import re
from ast import literal_eval as make_tuple
import os, os.path

def MoveListElement(list , element, index):
    # type: (list, object, int)
    list.remove(element)
    list.insert(index, element)
    return  list

def SerializeCommands(list, index):
    sys.stdout.write("Serializing . . . ")
    loop_indexer = 0
    output_text = []
    for elem in list:
        if isinstance(elem, Forward):
            text = """<class={0}, mul={1}>""".format("Forward", elem.mul)
            output_text.append(text+"\n")
        elif isinstance(elem, Backward):
            text = """<class={0}, mul={1}>""".format("Backward", elem.mul)
            output_text.append(text+"\n")
        elif isinstance(elem, Left):
            text = """<class={0}, mul={1}>""".format("Left", elem.mul)
            output_text.append(text+"\n")
        elif isinstance(elem, Right):
            text = """<class={0}, mul={1}>""".format("Right", elem.mul)
            output_text.append(text+"\n")
        elif isinstance(elem, PenDown):
            text = """<class={0}>""".format("PenDown")
            output_text.append(text+"\n")
        elif isinstance(elem, PenUp):
            text = """<class={0}>""".format("PenUp")
            output_text.append(text+"\n")
        elif isinstance(elem, PenWidth):
            text = """<class={0}, penwidth={1}>""".format("PenWidth", elem.pen_width)
            output_text.append(text+"\n")
        elif isinstance(elem, PenColor):
            ''' apro megjegyzes ide, tisztan lathato hogy egy tuple kerul kiirasra, az rgb kodokkal, ezert
                kis ugyeskedessel barmi szint ki lehet keverni, http://imgur.com/48JgYRM '''
            text = """<class={0}, pencolor={1}>""".format("PenColor", elem.pen_color)
            output_text.append(text+"\n")
        elif isinstance(elem, Home):
            text = """<class={0}>""".format("Home")
            output_text.append(text+"\n")
        elif isinstance(elem, FloodFill):
            text = """<class={0}>""".format("FloodFill")
            output_text.append(text+"\n")
        elif isinstance(elem, ShowTurtle):
            text = """<class={0}>""".format("ShowTurtle")
            output_text.append(text+"\n")
        elif isinstance(elem, HideTurtle):
            text = """<class={0}>""".format("HideTurtle")
            output_text.append(text+"\n")
        elif isinstance(elem, Loop):
            if elem.loop_id is None:
                elem.loop_id = loop_indexer
                elem.loopend.loop_id = loop_indexer
                loop_indexer += 1
            text = """<class={0}, loop_index={1}, cycle_number={2}>""".format("Loop", elem.loop_id, elem.cycle_number)
            output_text.append(text+"\n")
        elif isinstance(elem, LoopEnd):
            if elem.loop_id is None:
                elem.loop_id = loop_indexer
                elem.loopstart.loop_id = loop_indexer
                loop_indexer += 1
            text = """<class={0}, loop_index={1}>""".format("LoopEnd", elem.loop_id)
            output_text.append(text+"\n")
    print "Done"
    sys.stdout.write("Saving to file . . . ")
    open(os.path.join("UserData","data" + str(index) + ".dat"), "w").writelines(output_text)
    print "Done"

def LoadSerializedCommands(index):
    sys.stdout.write("Opening file . . . ")
    try:
        lines = open(os.path.join("UserData","data" + str(index) + ".dat"), "r").read().splitlines()
        print "Done"
    except:
        print "Error, no file found"
        return

    command_list = []

    for line in lines:
        command_dict = SplitCommand(line)
        if command_dict:
            command = None
            if command_dict['class'] == "Forward":
                command = Forward(vec2_pos=Vector2(0,0), size=(50, 50), mul=int(command_dict["mul"]))
            elif command_dict['class'] == "Backward":
                command = Backward(vec2_pos=Vector2(0, 0), size=(50, 50), mul=int(command_dict["mul"]))
            elif command_dict['class'] == "Left":
                command = Left(vec2_pos=Vector2(0, 0), size=(50, 50), mul=int(command_dict["mul"]))
            elif command_dict['class'] == "Right":
                command = Right(vec2_pos=Vector2(0, 0), size=(50, 50), mul=int(command_dict["mul"]))
            elif command_dict['class'] == "PenDown":
                command = PenDown(vec2_pos=Vector2(0,0), size=(50, 50))
            elif command_dict['class'] == "PenUp":
                command = PenUp(vec2_pos=Vector2(0, 0), size=(50, 50))
            elif command_dict['class'] == "PenWidth":
                command = PenWidth(vec2_pos=Vector2(0, 0), size=(50, 50))
                command.pen_width = int(command_dict["penwidth"])
            elif command_dict['class'] == "PenColor":
                command = PenColor(vec2_pos=Vector2(0, 0), size=(50, 50))
                command.SetColor(make_tuple(command_dict["pencolor"]))
            elif command_dict['class'] == "Home":
                command = Home(vec2_pos=Vector2(0, 0), size=(50, 50))
            elif command_dict['class'] == "FloodFill":
                command = FloodFill(vec2_pos=Vector2(0, 0), size=(50, 50))
            elif command_dict['class'] == "ShowTurtle":
                command = ShowTurtle(vec2_pos=Vector2(0, 0), size=(50, 50))
            elif command_dict['class'] == "HideTurtle":
                command = HideTurtle(vec2_pos=Vector2(0, 0), size=(50, 50))
            elif command_dict['class'] == "Loop":
                command = Loop(vec2_pos=Vector2(0, 0), size=(100, 50))
                command.loop_id = command_dict["loop_index"]
                command.SetCycleNumber(int(command_dict["cycle_number"]))
            elif command_dict['class'] == "LoopEnd":
                command = LoopEnd(vec2_pos=Vector2(0,0), size=(50, 50))
                command.loop_id = command_dict["loop_index"]
            command_list.append(command)

    # OsszeKotjuk a Loop es LoopEnd mezoket

    for elem in command_list:
        if isinstance(elem, Loop):
            for item in command_list:
                if isinstance(item, LoopEnd):
                    if item.loop_id == elem.loop_id:
                        elem.SetLoopend(item)
                        item.SetLoopStart(elem)
                        elem.loop_id = None
                        item.loop_id = None
                        break
        elif isinstance(elem, LoopEnd):
            for item in command_list:
                if isinstance(item, Loop):
                    if item.loop_id == elem.loop_id:
                        elem.SetLoopStart(item)
                        item.SetLoopend(elem)
                        elem.loop_id = None
                        item.loop_id = None
                        break
    return command_list

def SplitCommand(command):
    if re.match("<class=\w+(,\s\w+=(\d|\(\d{1,3}, \d{1,3}, \d{1,3}\)))*>", command) and command.startswith("<") and command.endswith(">"):
        command_dict = {}
        command = command[1:-1]
        lists_ = command.split(",")
        for attrbute in lists_:
            a = attrbute.split("=")
            try:
                command_dict[a[0].strip()] = a[1]
            except:
                command_dict[lists_[1].strip().split("=")[0]] = ", ".join(lists_[1:]).split("=")[1]
        return command_dict
    return None