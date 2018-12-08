from enum import Enum


class FieldToTestEnum(Enum):
    IDENTIFIER = 0
    ATTRIBUTE = 1
    VALUE = 2
    NO_TEST = 3


class TestNode:
    def __init__(self, fieldToTestEnum, value):
        self.fieldToTestEnum = fieldToTestEnum
        self.children = []
        self.outPutMemory = None
        self.value = value

    # def addCondition(self, condition):
    #     if self.isTopNode:
    #         for s in self.children:
    #             if condition.name == s.name:
    #                 s.addCondition(condition)
    #                 return
    #             tNode = TestNode(False, condition.name)
    #             self.children.append(tNode)
    #             tNode.addCondition(condition)
    #     else:
    #         for s in self.children:
    #             if s.name == condition.value:
    #                 return
    #         tNode = TestNode(False, condition.value)
    #         self.children.append(tNode)
    #         tNode.addAlphaMemory(condition)

    def addAlphaMemory(self, condition):
        self.outPutMemory = condition
