from src.Beta.ReteNode import ReteNode


class PNode(ReteNode):
    def __init__(self, parent, rule):
        super().__init__(parent)
        self.rule = rule
        self.ruleWmes=[]

    def isTopNode(self):
        return False

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
                self.ruleWmes.append(item.wme)
            parent.children = savedListOfChildren

    def getRuleName(self):
        return self.rule.name

    def isRuleUsed(self,workingMemory):
        for wme in workingMemory:
            if self.rule.hasAction(wme.attribute,[wme.symbol,wme.value]):
                return True
        return False

    def getGetWme(self):
        for wme in self.ruleWmes:
            print(wme)