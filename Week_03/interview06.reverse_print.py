# -*- coding: utf-8 -*-
__author__ = 'jack'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head):
        # 辅助栈方法
        stack = []
        res = []
        while head:
            stack.append(head.val)
            head = head.next
        # return stack[::-1]
        while len(stack) > 0:
            res.append(stack.pop())
        return res
        # res = []
        # while head:
        #     res.insert(0, head.val)
        #     head = head.next
        # return res