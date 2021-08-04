#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:28:48 2021

@author: vernet01
"""
import re
from Command import Command
from AddObj import AddObj
from DeleteObj import DeleteObj
from EditObj import EditObj
from IncorrectInputObj import IncorrectInputObj
from CommandObj import CommandObj


class ActionParser():
    def __init__(self, Parser):
        self.commandParser = Parser

    def parse(self, dataUser):
        userActionEnum = self.commandParser.parse(dataUser.command)
        if userActionEnum == Command.ADD:
            if dataUser.message is not None:
                return AddObj(userActionEnum, dataUser.message)
            else:
                return IncorrectInputObj(Command.USERERROR)
        elif userActionEnum == Command.DELETE:
            itemNb = self.handleInputConcernsNb(dataUser.message)
            if itemNb is None:
                return IncorrectInputObj(Command.USERERROR)
            return DeleteObj(userActionEnum, itemNb)
        elif userActionEnum == Command.EDIT:
            n = len(dataUser.message.split(" ", 1))
            if n >= 2:
                itemNb = self.handleInputConcernsNb(dataUser.message.split(" ", 1)[0])
                if itemNb is None:
                    return IncorrectInputObj(Command.USERERROR)
                newValue = dataUser.message.split(" ", 1)[1]
                return EditObj(userActionEnum, itemNb, newValue)
            else:
                return IncorrectInputObj(Command.USERERROR)
        else:
            return CommandObj(userActionEnum)

    def handleInputConcernsNb(self, message):
        is_int = re.search("^[0-9]+$", message)
        if is_int is None:
            return None
        return int(message)
