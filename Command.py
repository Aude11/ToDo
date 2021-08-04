#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:15:20 2021

@author: vernet01
"""
import enum


class Command(enum.Enum):
    ADD = 1
    QUIT = 2
    DELETE = 3
    EDIT = 4
    NONE = 5
    USERERROR = 6
