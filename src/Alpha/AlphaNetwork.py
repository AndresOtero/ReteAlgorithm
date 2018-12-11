from src.Alpha.TestNode import TestNode


class AlphaNetwork():
    def __init__(self):
        self.topNode = TestNode(True, "Top Node")

    def addCondition(self, condition):
        self.topNode.addCondition(condition)

    def addWME(self, wme):
        self.constantTestNodeActivation(self.topNode, wme)

    def constantTestNodeActivation(self, node, wme):
        if not node.isTopNode:
            attr = wme.attribute
            if attr == node.name:
                for s in node.sons:
                    self.constantTestNodeActivation(self, s, wme)
            value = wme.value
            if value == node.name:
                node.alphaMemory.addIfCompare(wme)
            else:
                return
        if node.alphaMemory:
            self.alphaMemoryActivation(node.alphaMemory, wme)
