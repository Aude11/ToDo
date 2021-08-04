#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:37:43 2021

@author: vernet01
"""
from CommandObj import CommandObj


class IncorrectInputObj(CommandObj):
    def __init__(self, command):
        CommandObj.__init__(self, command)
        self.command = command
