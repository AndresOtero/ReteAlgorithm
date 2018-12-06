
class TestNode:
    def __init__(self, isTopNode, name):
        self.isTopNode = isTopNode
        self.sons = []
        self.alphaMemory = None
        self.name = name

    def addCondition(self, condition):
        if self.isTopNode:
            for s in self.sons:
                if condition.name == s.name:
                    s.addCondition(condition)
                    return
                tNode = TestNode(False, condition.name)
                self.sons.append(tNode)
                tNode.addCondition(condition)
        else:
            for s in self.sons:
                if s.name == condition.value:
                    return
            tNode = TestNode(False, condition.value)
            self.sons.append(tNode)
            tNode.addAlphaMemory(condition)

    def addAlphaMemory(self, condition):
        self.alphaMemory = condition
