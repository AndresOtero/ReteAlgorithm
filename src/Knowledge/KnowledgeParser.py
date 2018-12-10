import csv

from src.Knowledge.Knowledge import Knowledge
Symbols = [" < ", " > ", " >= ", " <= ", " = "]


class KnowledgeParser:
    @staticmethod
    def getKnowledges(fileName):
        knowleadge=Knowledge()
        with open(fileName) as rulesFiles:
            for line in rulesFiles:
                line = line.strip("\n")
                for s in Symbols:
                    if s in line:
                        premise = line.split(s)
                        conditionSymbol = s
                        break
                attributeName = premise[0]
                value = premise[1]
                knowleadge.addAttribute(attributeName,symbol=conditionSymbol,value=value)
        return knowleadge
