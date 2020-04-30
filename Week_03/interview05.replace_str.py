# -*- coding: utf-8 -*-
__author__ = 'jack'

class Solution:
    def replaceSpace(self, s: str) -> str:
        return '%20'.join(s.split(' '))