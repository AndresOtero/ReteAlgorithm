from src.Beta.ReteNode import ReteNode
from src.Beta.Token import Token


class BetaMemory(ReteNode):
    def __init__(self, parent):
        self.items = []
        super().__init__(parent)
        self.allChildren = []

    def isBetaMemoryNode(self):
        return True

    def leftActivation(self, token, wme):
        newToken = Token(node=self, parent=token, wme=wme)
        self.items.insert(0, newToken)
        for child in self.children:
            child.leftActivation(newToken)

    @staticmethod
    def buildOrShareBetaMemory(parent):
            for child in parent.children:
                if child.isBetaMemoryNode():
                    return child
            betaMemory= BetaMemory(parent)
            parent.children.insert(0,betaMemory)
            betaMemory.updateNewNodeWithMatchesFromAbove()