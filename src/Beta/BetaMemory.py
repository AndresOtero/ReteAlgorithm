from src.Beta.ReteNode import ReteNode
from src.Beta.Token import Token


class BetaMemory(ReteNode):
    def __init__(self, parent):
        super().__init__(parent)
        self.items = []

    def leftActivation(self, token, wme):
        newToken = Token(token, wme)
        self.items.append(newToken)
        for child in self.children:
            child.leftActivation(newToken)

    def isBetaMemory(self):
        return True

    @staticmethod
    def buildOrShareBetaMemoryNode(parent):
        for child in parent.children:
            if child.isBetaMemory():
                return child
        betaMemory=BetaMemory(parent)
        betaMemory.updateNewNodeWithMatchesFromAbove()
        return betaMemory

    def updateNewNodeWithMatchesFromAbove(self):
        for token in self.parent.amem.items:
            self.leftActivation(token)


