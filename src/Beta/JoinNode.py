from src.Beta.ReteNode import ReteNode
from src.Beta.Token import Token


class JoinNode(ReteNode):
    def __init__(self, parent, amem, tests):
        super().__init__(parent)
        self.amem = amem
        self.name = amem.condition.name
        self.value = amem.condition.value
        self.tests = tests
        self.children = []
        self.isTopNode= False

    def rightActivation(self, wme):
        for t in self.parent.items:
            if self.performJoinTests(t, wme):
                for child in self.children:
                    child.leftActivation(t, wme)

    def leftActivation(self, token):
        for item in self.amem.items:
            if self.performJoinTests(token, item.wme):
                for child in self.children:
                    child.leftActivation(token, item.wme)

    def performJoinTests(self, t, wme):
        raise Exception()

    def isJoinNode(self):
        return True

    @staticmethod
    def buildOrShareJoinNode(parent, alphaMemory, tests):
        for child in parent.children:
            if child.isJoinNode():
                if child.amem == alphaMemory and child.tests == tests:
                    return child
        joinNode = JoinNode(parent, alphaMemory, tests)
        parent.children.insert(0, joinNode)
        alphaMemory.succesors.insert(0, joinNode)
        return joinNode

