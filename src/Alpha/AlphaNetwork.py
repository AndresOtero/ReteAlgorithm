from src.Alpha.AlphaMemory import AlphaMemory
from src.Alpha.TestNode import TestNode
from src.Beta.BetaMemory import BetaMemory
from src.Beta.JoinNode import JoinNode
from src.Beta.PNode import PNode
from src.Beta.TestAtJoinNode import TestAtJoinNode


class AlphaNetwork():
    def __init__(self):
        self.topNode = TestNode(True, "Top Node")
        self.workingMemory = []
        self.pNodes=[]

    def addCondition(self, condition):
        self.topNode.addCondition(condition)

    def addWME(self, wme):
        self.workingMemory.append(wme)
        self.constantTestNodeActivation(self.topNode, wme)

    def removeWME(self, wme):
        for item in wme.alphaMemsItems:
            item.amem.remove(wme)
        while len(wme.tokens) != 0:
            wme.tokens[0].deleteTokenAndDescendents()

    def constantTestNodeActivation(self, node, wme):
        if not node.isTopNode:
            attr = wme.attribute
            if attr == node.name:
                for child in node.children:
                    self.constantTestNodeActivation(child, wme)
            value = wme.value
            if value == node.name:
                node.alphaMemory.addIfCompare(wme)
            else:
                return
        for child in node.children:
            self.constantTestNodeActivation(child, wme)

    def buildOrShareAlphaMemory(self, condition):
        currentNode = self.topNode
        currentNode = self.buildOrShareConstantTestNode(currentNode, condition)
        if currentNode.alphaMemory is not None:
            return currentNode.alphaMemory
        am = AlphaMemory(condition)
        currentNode.alphaMemory = am
        for w in self.workingMemory:
            am.addIfCompare(wme=w)
        return am

    @staticmethod
    def buildOrShareConstantTestNode(parent, condition):
        tnode = parent.addCondition(condition)
        return tnode

    def addProduction(self, Rule):
        lhs=Rule.getConditions()
        currentNode = self.topNode
        earlierConditions = []
        tests = currentNode.addCondition(lhs[0])
        am = self.buildOrShareAlphaMemory(lhs[0])
        currentNode = JoinNode.buildOrShareJoinNode(currentNode, am, tests)
        for i in range(1,len(lhs)):
            currentNode=BetaMemory.buildOrShareBetaMemoryNode(currentNode)
            earlierConditions.append(lhs[i-1])
            tests=TestAtJoinNode.getJoinTestFromCondition(lhs[i],earlierConditions)
            am=self.buildOrShareAlphaMemory(lhs[i])
            currentNode=JoinNode.buildOrShareJoinNode(currentNode,am,tests)
        pNode=PNode(currentNode,Rule)
        currentNode.children.append(pNode)
        pNode.updateNewNodeWithMatchesFromAbove()
        self.pNodes.append(pNode)
