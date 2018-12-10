from src.Condition.ConditionFactory import ConditionFactory
from src.Rules.Rule import Rule

Symbols = [" < ", " > ", " >= ", " <= ", " = "]


class RulesParser:
    @staticmethod
    def getRules(fileName):
        listRules = []
        arePremises = False
        areActions = False
        with open(fileName) as rulesFiles:
            for line in rulesFiles:
                line = line.strip("\n")
                if ")" in line:
                    listRules += rules
                    areActions = False
                if "-->" in line:
                    areActions = True
                    arePremises = False
                    rules.append(rule)
                    continue
                if arePremises:
                    if "O" in line:
                        line = line.strip("O ")
                        rules.append(rule)
                        rule = Rule(ruleName)
                    if "Y" in line:
                        line = line.strip("Y ")
                    for s in Symbols:
                        if s in line:
                            premise = line.split(s)
                            conditionSymbol = s
                            break
                    attributeName = premise[0]
                    value = premise[1]
                    condition = ConditionFactory.createCondition(attributeName, conditionSymbol, value)
                    rule.addPremise(attributeName, condition)
                if areActions:
                    for s in Symbols:
                        if s in line:
                            action = line.split(s)
                            conditionSymbol = s
                    attributeName = action[0]
                    value = action[1]
                    for rule in rules:
                        rule.addAction(attributeName, conditionSymbol,value)
                if "(" in line:
                    arePremises = True
                    ruleName = line.strip("(")
                    rules = []
                    rule = Rule(ruleName)
        return listRules
