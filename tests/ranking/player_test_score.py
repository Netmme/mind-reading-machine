#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PlayerTestScore():
    def __init__(self, name, mean=1600, std_dev=8):
        self.mean = mean
        self.std_dev = std_dev
        self.name = name

    def set_score(self, new_score):
        self.mu = self.mu + new_score

    def present(self, full):
        print('My name is', self.name)
        if full:
            print('My mean is', self.mean)
            print('My std deviation is', self.std_dev)
