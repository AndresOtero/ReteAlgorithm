class ReteNode:
    def __init__(self, parent):
        self.children = []
        self.parent = parent

    def isBetaMemory(self):
        return False

    def isJoinNode(self):
        return False

    def updateNewNodeWithMatchesFromAbove(self):
        pass