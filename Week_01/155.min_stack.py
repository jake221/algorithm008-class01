# -*- coding: utf-8 -*-
__author__ = 'jack'


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        if len(self._min_stack) == 0:
            self._min_stack.append(x)
        elif x < self._min_stack[0]:
            self._min_stack.pop()
            self._min_stack.append(x)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

        if len(self._stack) > 0:
            min = self._stack[0]
            for element in self._stack:
                if element <= min:
                    min = element
            self._min_stack.append(min)


    def top(self) -> int:
        return self._stack[-1]


    def getMin(self) -> int:
        return self._min_stack[0]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(-6)
obj.push(-2)
obj.push(-3)
obj.push(-4)

obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print()
print(param_3, param_4)
