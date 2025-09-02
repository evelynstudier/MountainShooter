#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.game_mode = game_mode
        self.name = name
        self.entity_list: list[Entity] = []

    def run(self, ):
        pass
