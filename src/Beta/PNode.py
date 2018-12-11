from src.Beta.ReteNode import ReteNode


class PNode(ReteNode):
    def __init__(self, parent, rule):
        super().__init__(parent)
        self.rule = rule

    def isTopNode(self):
        return  False

    def updateNewNodeWithMatchesFromAbove(self):
        parent = self.parent
        if parent.isBetaMemory():
            for tok in parent.items:
                print("updateNewNodeWithMatchesFromAbove", tok)
        if parent.isJoinNode():
            savedListOfChildren = parent.children
            parent.children = [self]
            for item in parent.amem.items:
                parent.rightActivation(item.wme)
            parent.children = savedListOfChildren
