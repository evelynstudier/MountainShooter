#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = None
        self.surf = None
        self.rect = None

    def move(self, ):
        pass
