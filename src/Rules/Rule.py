class Rule:
    # noinspection SpellCheckingInspection
    def __init__(self, name):
        self.premises = []
        self.actionsDicc = {}
        self.name = name

    def getAction(self, key):
        return self.actionsDicc[key]

    @staticmethod
    def knowledgeMeetsGivenPremise(knowledge, attributeKey, premise):
        if not knowledge.hasAttribute(attributeKey):
            return False
        return False if attributeKey not in premise else premise[attributeKey].compare(knowledge, attributeKey)

    def meetsPremises(self, knowledge):
        return all(
            [self.knowledgeMeetsGivenPremise(knowledge, key, premise) for premise in self.premises for key in premise])

    def fireRule(self, knowledge):
        for key in self.actionsDicc:
            knowledge.addAttribute(key, self.getActionSymbol(key),self.getActionValue(key))

    def hasAction(self, actionKey, actionValue):
        return False if actionKey not in self.actionsDicc else self.actionsDicc[actionKey] == actionValue

    def addPremise(self, key, value):
        self.premises.append({key: value})

    def addAction(self, key, symbol, value):
        self.actionsDicc[key] = [symbol, value]

    def getActionValue(self, key):
        return self.actionsDicc[key][1]

    def getActionSymbol(self, key):
        return self.actionsDicc[key][0]

    def getConditions(self):
        conditions=[]
        for premise in self.premises:
            for key in premise:
                conditions.append(premise[key])
        return conditions

    def __eq__(self, other):
        return self.premises == other.premises and self.actionsDicc == other.actionsDicc

    def __str__(self):
        return str("Name ") + str(self.name) + str("Premises ") + str(self.premises) + str("Actions ") + str(
            self.actionsDicc)
