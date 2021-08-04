#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:54:08 2021

@author: vernet01
"""
from CommandObj import CommandObj


class AddObj(CommandObj):
    def __init__(self, command, itemToAdd):
        CommandObj.__init__(self, command)
        self.itemToAdd = itemToAdd
