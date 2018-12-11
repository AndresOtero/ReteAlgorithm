from src.Alpha.AlphaMemory import AlphaMemory


class TestNode:
    def __init__(self, isTopNode, name):
        self.isTopNode = isTopNode
        self.children = []
        self.alphaMemory = None
        self.name = name

    def addCondition(self, condition):
        if self.isTopNode:
            for s in self.children:
                if s.isJoinNode():
                    pass
                elif condition.name == s.name:
                    s.addCondition(condition)
                    return s
            tNode = TestNode(False, condition.name)
            self.children.append(tNode)
            tNode.addCondition(condition)
        else:
            for s in self.children:
                if s.name == condition.value:
                    return s
            tNode = TestNode(False, condition.value)
            self.children.append(tNode)
            tNode.addAlphaMemory(condition)
        return tNode

    def addAlphaMemory(self, condition):
        self.alphaMemory = AlphaMemory(condition)

    def isJoinNode(self):
        return False