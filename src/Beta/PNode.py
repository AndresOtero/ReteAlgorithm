from src.Beta.ReteNode import ReteNode
from src.Beta.Token import Token


class PNode(ReteNode):
    def __init__(self, parent, production):
        self.items = []
        self.production = production
        super().__init__(parent)

    def leftActivation(self, token, wme):
        newToken = Token(token, wme)
        self.items.insert(0, newToken)
        for child in self.children:
            child.leftActivation(newToken)
