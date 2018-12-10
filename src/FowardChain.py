class FowardChain:
    def __init__(self, rules, knowledge):
        self.knowledge = knowledge
        self.rules = rules
        self.usedRules = []

    def runReteAlgorithm(self):
        runAgain = True
        while runAgain:
            runAgain = self.fireRule()

    def fireRule(self):
        eureka = False
        rulesToRemove = []
        for rule in self.rules:
            if eureka:
                break
            elif rule.meetsPremises(self.knowledge):
                rule.fireRule(self.knowledge)
                self.usedRules.append(rule)
                eureka = True
        self.rules = [rule for rule in self.rules if rule not in self.usedRules]
        return eureka

    def getUsedRules(self):
        return self.usedRules

    def printUsedRules(self):
        print("Las reglas utilizadas fueron:")
        for rule in self.usedRules:
            print(" - "+rule.name)