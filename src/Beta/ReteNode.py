from abc import ABC


class ReteNode(ABC):
    def __init__(self, parent):
        self.children = []
        self.parent = parent

    def isBetaMemoryNode(self):
        return False