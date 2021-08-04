#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 23:23:02 2021

@author: vernet01
"""
from CommandObj import CommandObj


class DeleteObj(CommandObj):
    def __init__(self, command, itemNb):
        CommandObj.__init__(self, command)
        self.itemNb = itemNb
