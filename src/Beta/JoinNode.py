from src.Beta.ReteNode import ReteNode


class JoinNode(ReteNode):
    def __init__(self, ameme, parent):
        self.alphaMem = ameme
        self.tests = []
        super().__init__(parent)
        self.nearestAncestorWithSameAmem = None

    def leftActivation(self, token):
        if self.parent:
            self.relinkToAlphaMemory()
            if not self.alphaMem.items:
                self.parent.children.remove(self)
        for w in self.alphaMem.items:
            if self.performJoinTests(token, w):
                for child in self.children:
                    child.leftActivation(token, w)

    def rightActivation(self, wme):
        if self.alphaMem:
            self.relinkToBetaMemory()
            if not self.parent.items:
                self.alphaMem.succesors.remove(self)
        for t in self.parent.items:  # Parent is the beta Memory
            if self.performJoinTests(t, wme):
                for child in self.children:
                    child.leftActivation(t, wme)

    def performJoinTests(self, token, wme):
        for test in self.tests:
            arg1 = wme.get(test.fieldOfArg1)
            wme2 = token.wme
            arg2 = wme2.get(test.fieldOfArg2)
            if arg1 != arg2:
                return False
        return True

    def relinkToAlphaMemory(self):
        ancestor = self.nearestAncestorWithSameAmem
        while ancestor is not None and ancestor.isRightUnlinked():  # todo
            ancestor = ancestor.nearestAncestorWithSameAmem
        if ancestor is not None:
            succesors = self.alphaMem.succesors
            index = succesors.index(ancestor)
            succesors.insert(index, self)
        else:
            self.alphaMem.succesors.append(self)

    def relinkToBetaMemory(self):
        self.parent.children.insert(0, self)
